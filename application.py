import os
import httplib2
import json
import datetime
import random
import string
import requests
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, jsonify, make_response, g
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_create import Base, Category, Product, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError


app = Flask(__name__)

# Taken from ud330 and Oauth project (Udacity)
# Connect to database.
engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine

# Create database session.
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Authentication
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Buy the best Product Catalog App"


# Taken from ud330 and Oauth project (Udacity)
@app.route('/login')
def showLogin():
    """

    Creates a state token to prevent request forgery. Stores it in the
    session for later validation.
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Taken from ud330 and Oauth project (Udacity)
@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Gmail authentication.

    Gathers data from Google Sign In API
    and places it inside a session variable.
    """
    # Validate state token.
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code.
    code = request.data

    try:
        # Updgrade the authorization code into a credentials object.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check to see if user is already logged in.
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info from API.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['provider'] = 'google'
    login_session['username'] = data["name"]
    login_session['picture'] = data["picture"]
    login_session['email'] = data["email"]

    # See if user exists, if he/she doesn't make a new one.
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h4>Welcome, '
    output += login_session['username']
    output += '!</h4>'
    output += '<img src="'
    output += login_session['picture']
    output += ' "style = "width: 200px; height: 200px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    return output


# Taken from ud330 and Oauth project (Udacity)
def createUser(login_session):
    """User helper functions.

    These functions serve as local permission system.
    """
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        image=login_session['picture'])

    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()

    return newUser.id


# Taken from ud330 and Oauth project (Udacity)
def getUserInfo(user_id):
    """Returns the user_id from the session."""
    user = session.query(User).filter_by(id=user_id).one()
    return user.id


# Taken from ud330 and Oauth project (Udacity)
def getUserID(email):
    """Filters the user by their e-mail."""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except RuntimeError:
        return None


# Taken from ud330 and Oauth project (Udacity)
@app.route('/gdisconnect')
def gdisconnect():
    """Revokes a current user's Google+ token and reset their login session."""
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(json.dumps('Current user not'
                                            'connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s'\
        % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # reset the user's session.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Succesfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("You have successfully been logged out.")
        return redirect(url_for('default'))
    else:
        # For whatever reason the given token was invalid.
        response = make_response(json.dumps('Failed to revoke'
                                            'token for given user'), 400)
        response.headers['Content-Type'] = 'application/json'
        flash("You are currently not logged in!")
        return redirect(url_for('default'))


# using a decorator function here to reduce DRY
def login_mandatory(f):
    """Login decorater function."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            flash('You need to be logged in to view this content')
            return redirect('/default')
        return f(*args, **kwargs)
    return decorated_function


# JSON output of whole catalog
@app.route('/catalog.json')
def outputFullCatalogAsJson():
    """Makes an API endpoint for the database."""
    categories = session.query(Category).all()
    catalog = []
    for c in categories:
        catalog.append(c.serialize)
        products = session.query(Product).filter_by(category_id=c.id).all()
        catalog[-1]['Products'] = [p.serialize for p in products]
    return jsonify(Categories=catalog)


#
# CRUD operations start
#
# Read operation
@app.route('/')
@app.route("/category/")
def default():
    """Default page route."""
    categories = session.query(Category).order_by(asc(Category.id))
    latest = session.query(Product).order_by(
        Product.created_at.desc()).limit(8).all()
    return render_template('index.html', categories=categories, latest=latest)


# Read operation
@app.route('/category/<int:category_id>/')
def showCategory(category_id):
    """Category page route."""
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).order_by(asc(Category.id))
    products = session.query(Product).filter_by(category_id=category.id)
    return render_template(
        'categories.html', category=category, products=products,
        categories=categories)


# Read operation
@app.route("/category/<int:category_id>/<int:product_id>")
def showProduct(category_id, product_id):
    """Show product route."""
    category = session.query(Category).filter_by(id=category_id).one()
    product = session.query(Product).filter_by(id=product_id).one()
    return render_template(
        'showProduct.html', product=product,
        category=category)


# Create operation
@app.route('/category/<int:category_id>/new/', methods=['GET', 'POST'])
@login_mandatory
def newProduct(category_id):
    """Route for creating a new Product."""
    if request.method == 'POST':
        newProduct = Product(
            name=request.form['name'],
            description=request.form['description'],
            created_at=datetime.datetime.now(),
            category_id=category_id,
            user_id=login_session['user_id'])

        session.add(newProduct)
        session.commit()
        flash("New product '" + newProduct.name + "' has been added")
        return redirect(url_for(
            'showProduct', category_id=category_id, product_id=newProduct.id))
    else:
        categories = session.query(Category).all()
        return render_template(
            'newProduct.html', categories=categories, category_id=category_id)


# Update Operation
@app.route('/category/<int:category_id>/'
           '<int:product_id>/edit/', methods=['GET', 'POST'])
@login_mandatory
def editProduct(category_id, product_id):
    """Route for editig a Product."""

    editedProduct = session.query(Product).filter_by(id=product_id).one()
    creator = getUserInfo(editedProduct.user_id)

    if editedProduct.user_id != creator:
        return redirect(
            'showProduct', category_id=category.id,
            product_id=editedProduct.id)
    if request.method == 'POST':
        if request.form['name']:
            editedProduct.name = request.form['name']
        if request.form['description']:
            editedProduct.description = request.form['description']
        session.add(editedProduct)
        session.commit()
        flash("Product '" + editedProduct.name + "' edited succesfully!")
        return redirect(url_for(
            'showProduct', category_id=category_id,
            product_id=editedProduct.id))
    else:
        categories = session.query(Category).all()
        return render_template(
            'editProduct.html', category_id=category_id,
            product_id=product_id, p=editedProduct, categories=categories)


# Caution : Delete operation
@app.route('/category/<int:category_id>/<int:product_id>/delete/',
           methods=['GET', 'POST'])
@login_mandatory
def deleteProduct(category_id, product_id):
    """Route for deleting a product."""
    productToDelete = session.query(Product).filter_by(id=product_id).one()
    creator = getUserInfo(productToDelete.user_id)
    if productToDelete.user_id != creator:
        return redirect('showProduct', category_id=category.id,
                        product_id=productToDelete.id)
    if request.method == 'POST':
        session.delete(productToDelete)
        session.commit()
        flash("Product '" + productToDelete.name + "' deleted succesfully!")
        return redirect(url_for('default', category_id=category_id))
    else:
        return render_template('deleteProduct.html', product=productToDelete)

# CRUD operations end


# Taken from ud330. Changed port to 8000 as per specifications.
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
