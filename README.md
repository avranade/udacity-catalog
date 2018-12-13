## Udacity Fullstack Nanodegree - Product Catalog App

The Product catalog allows users to interact with the database after authentication. Authenticated Users can create, update and delete their records. 

## Project Overview
You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


## Technologies used
Backend: Python Flask SQLAlchemy
Frontend: HTML, CSS, JS. Fontawesome was used for the Home Icon on Page. 

## Implementation
* Code for this project is based on the ud330 and Oauth project code as part of the lessons. Some code has been modified, whereas some has been kept as is. Boilerplate gconnect, gdisconnect etc are taken as is. 
* UI is basic Bootstrap with some customizations. 
* As part of the design decision, data is first populated in the database and then interacted with. 
* Users do not have the capability to create categories, just Products. One category can have multiple products. 
* Google sign in is used for Authentication. FB signin, while useful, hasn't been used here. 
* Users can sign up using Google only. Once signed in, users can edit/delete only the content they created. 
* A json endpoint at /catalog.json is kept open so that an API call can be made to it. 

## Installation and How to View This App
1. Install Vagrant and VirtualBox
2. Clone the repository
3. Launch and connect to the Vagrant VM 
```
	* Navigate to location of vagrantfile

    vagrant up
    vagrant ssh
```
4. Setup and initially populate the database
```
    # Navigate to the catalog folder inside the Vagrant folder
    python database_create.py
    python lotsofproducts.py
```
5. Run the application
```
    python application.py
```
6. Access the application
Visit [http://localhost:8000](http://localhost:8000) as specified to test locally.

7. Add Google client ID and client secret to client_secrets.json for Oauth . 
8. Make sure you also update client ID in login.html, otherwise the Oauth call fails 

## Google credentials file
* Go to https://console.cloud.google.com/apis/credentials/oauthclient and setup Google OAuth API Credentials. 
* Enter ```http://localhost:8000``` in the Authorized JavaScript origins and ```http://localhost:8000/login and http://localhost:8000/gconnect``` in the Authorized redirect URIs.
* Save, download JSON and rename the file to ```client_secrets.json``` and replace the file with the same name in the project directory.

## Rubric

|SECTION|CRITERIA|SPECS. MET?|
|---|---|---|
| API Endpoints | Does the project implement a JSON endpoint with all required content? | Yes|
| CRUD: Read | Does the website include a form to update a record in the database and correctly processes this form? | Yes |
| CRUD: Create | Does the website include a form allowing users to add new items and correctly processes these forms? | Yes |
| CRUD: Update | Does the website include a form to update a record in the database and correctly processes this form? | Yes |
| CRUD: Delete | Does the website include a way to delete an item from the catalog? | Yes |
| Authentication & Authorization | Do create, delete, and update operations consider authorization status prior to execution? | Yes | 
| Authentication & Authorization | Does the website implement a third party authentication and authorization service? | Yes |
| Authentication & Authorization | Is there a “login” and “logout” button/link in the website? | Yes |
| Code Quality | Is the code ready for personal review and is neatly formatted? | Yes. Pycodestyle has been used to remove Pep-8 violations |
| Comments | Are comments present and effectively explain longer code procedures? | Yes, wherever required. |
| Documentation | Is there a README file included detailing all steps required to successfully run the application? | Yes |



## Helpful Resources
* [Google OAuth Credentials](https://console.cloud.google.com/apis/credentials/oauthclient)
* [Facebook Deveopers](https://developers.facebook.com/apps)
* [PEP8 online checker](http://pep8online.com/)
* [Flask SQL Alchemy Documentation](http://flask-sqlalchemy.pocoo.org/2.3/)