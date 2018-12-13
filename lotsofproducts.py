#!/usr/bin/python
# -*- coding: utf-8 -*-
# Based on ud330 and Oauth project code from Udacity

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_create import Base, User, Category, Product

engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

user1 = User(name='Test User', email='test_user@gmail.com')

category1 = Category(name='Appliances')
category2 = Category(name='TV & Home theater')
category3 = Category(name='Computer & Tablets')
category4 = Category(name='Cameras & Camcorders')
category5 = Category(name='Cellphones')
category6 = Category(name='Audio')
category7 = Category(name='Video Games')
category8 = Category(name='Movies & Music')
category9 = Category(name='Car Electronics & GPS')
category10 = Category(name='Wearables')
category11 = Category(name='Health, Fitness & Beauty')
category12 = Category(name='Home, Garage & Office')
category13 = Category(name='Smart Home')

db_session.add(category1)
db_session.add(category2)
db_session.add(category3)
db_session.add(category4)
db_session.add(category5)
db_session.add(category6)
db_session.add(category7)
db_session.add(category8)
db_session.add(category9)
db_session.add(category10)
db_session.add(category11)
db_session.add(category12)
db_session.add(category13)

db_session.commit()

product1 = Product(
    name='Refridgerators',
    description='These keep things cool',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product2 = Product(
    name='Dishwashers',
    description="These wash dishes so you don't have to",
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product3 = Product(
    name='Ranges, Cook tops & Wall Ovens',
    description='These are used to cook and bake things',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product4 = Product(
    name='Range Hoods & Ventilation',
    description='Just in case you burn something',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product5 = Product(
    name='Microwaves',
    description='When you want to cook in a hurry',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product6 = Product(
    name='Kegerators & Wine coolers',
    description='You probably will have one too many',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product7 = Product(
    name='Freezers & Ice Makers',
    description='When you need to freeze things or make ice cubes',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product8 = Product(
    name='Smart Appliances',
    description='Not so smart if you ask me',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product9 = Product(
    name='Washers & Dryers',
    description="Coz I don't want to wash my own clothes",
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category1,
    user=user1,
    )

product10 = Product(
    name='75 inch or larger TVs',
    description='You would need to buy a movie theater',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category2,
    user=user1,
    )

product11 = Product(
    name='4K Ultra HD TVs',
    description='Pimples and Pores, now in 4K',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category2,
    user=user1,
    )

product12 = Product(
    name='OLED TVs',
    description='Your rich friends have these',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category2,
    user=user1,
    )

product13 = Product(
    name='Home Theater systems',
    description='When you really want to wake up the neighbors',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category2,
    user=user1,
    )

product14 = Product(
    name='Sound bars',
    description='Home theater dreams, real world money',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category2,
    user=user1,
    )

product15 = Product(
    name='Laptops',
    description='Who even uses a desktop anymore',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product16 = Product(
    name='Desktops',
    description='I stand corrected',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product17 = Product(
    name='iPad',
    description='To watch movies in bed',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product18 = Product(
    name='VR Headsets',
    description='Avoiding people in a new way',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product19 = Product(
    name='Monitors',
    description='To connect to those PCs that I thought no one was using',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product20 = Product(
    name='Printers',
    description='To print those Government required forms',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category3,
    user=user1,
    )

product21 = Product(
    name='Digital SLR Cameras',
    description='Pretend to know what you are doing',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category4,
    user=user1,
    )

product22 = Product(
    name='Mirrorless Cameras',
    description="You don't do anything and then pretend to know you did",
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category4,
    user=user1,
    )

product23 = Product(
    name='Point & Shoot Cameras',
    description='They do what everyone else with DSLRs is actually doing',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category4,
    user=user1,
    )

product24 = Product(
    name='Action Camcorders',
    description='Sitting in one place is overrated',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category4,
    user=user1,
    )

product25 = Product(
    name='Memory Cards',
    description='The thing you forget to put in your camera',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category4,
    user=user1,
    )

product26 = Product(
    name='iPhone',
    description='Shut up and take my money',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category5,
    user=user1,
    )

product27 = Product(
    name='Samsung Galaxy',
    description='Shut up again and take my money',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category5,
    user=user1,
    )

product28 = Product(
    name='Phone accessories',
    description='The multiple cables and dongles that you need',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category5,
    user=user1,
    )

product29 = Product(
    name='Home Theater systems',
    description='They are listed here as well',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category6,
    user=user1,
    )

product30 = Product(
    name='Headphones',
    description='Annoying, and yet not disturbing anyone',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category6,
    user=user1,
    )

product31 = Product(
    name='Portable speakers',
    description='Coz why not',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category6,
    user=user1,
    )

product32 = Product(
    name='Xbox one',
    description='Coz Microsoft',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category7,
    user=user1,
    )

product33 = Product(
    name='PS4',
    description='Coz Sony',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category7,
    user=user1,
    )

product34 = Product(
    name='Nintendo',
    description='Coz Mario',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category7,
    user=user1,
    )

product35 = Product(
    name='Blu-ray discs',
    description='Pores and Pimples in hi def',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category8,
    user=user1,
    )

product36 = Product(
    name='Star Wars',
    description='These are not the droids...you know the rest',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category8,
    user=user1,
    )

product37 = Product(
    name='Harry Potter',
    description='Who wants to grow up?',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category8,
    user=user1,
    )

product38 = Product(
    name='APPLE watch',
    description='Tell your friends how it is the best',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category10,
    user=user1,
    )

product39 = Product(
    name='Garmin GPS',
    description="You'll thank me when you get lost in the mountains",
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category9,
    user=user1,
    )

product40 = Product(
    name='Fitbit',
    description='Focus on fitness at half the cost of an Apple watch',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category10,
    user=user1,
    )

product41 = Product(
    name='Blood Pressure Monitors',
    description='Wait till you see the price',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category11,
    user=user1,
    )

product42 = Product(
    name='Garage Door openers',
    description='Batcave phase 1',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category12,
    user=user1,
    )

product43 = Product(
    name='WIFI routers',
    description='Have you tried turning it off and on again?',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category13,
    user=user1,
    )

product44 = Product(
    name='Motion Sensor',
    description='Who moved my cheese?',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category13,
    user=user1,
    )

product45 = Product(
    name='Voice Assistants',
    description='This is how Skynet begins',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category13,
    user=user1,
    )

product46 = Product(
    name='Telephones',
    description='yeah... I know',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category12,
    user=user1,
    )

product47 = Product(
    name='Projector',
    description='When 75 inch screens are too small',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category12,
    user=user1,
    )

product48 = Product(
    name='Windows XP',
    description='The best Windows ever made',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category12,
    user=user1,
    )

product49 = Product(
    name='Shavers',
    description='No time for a razor',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category11,
    user=user1,
    )

product50 = Product(
    name='Thermometers',
    description='Coz you keep saying you are Hot or you are cool',
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    category=category11,
    user=user1,
    )

db_session.add(product1)
db_session.add(product2)
db_session.add(product3)
db_session.add(product4)
db_session.add(product5)
db_session.add(product6)
db_session.add(product7)
db_session.add(product8)
db_session.add(product9)
db_session.add(product10)
db_session.add(product11)
db_session.add(product12)
db_session.add(product13)
db_session.add(product14)
db_session.add(product15)
db_session.add(product16)
db_session.add(product17)
db_session.add(product18)
db_session.add(product19)
db_session.add(product20)
db_session.add(product21)
db_session.add(product22)
db_session.add(product23)
db_session.add(product24)
db_session.add(product25)
db_session.add(product26)
db_session.add(product27)
db_session.add(product28)
db_session.add(product29)
db_session.add(product30)
db_session.add(product31)
db_session.add(product32)
db_session.add(product33)
db_session.add(product34)
db_session.add(product35)
db_session.add(product36)
db_session.add(product37)
db_session.add(product38)
db_session.add(product39)
db_session.add(product40)
db_session.add(product41)
db_session.add(product42)
db_session.add(product43)
db_session.add(product44)
db_session.add(product45)
db_session.add(product46)
db_session.add(product47)
db_session.add(product48)
db_session.add(product49)
db_session.add(product50)

db_session.commit()

print 'Added all Categories and Products!'
