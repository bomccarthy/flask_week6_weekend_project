from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

cartTable = db.Table(
    'cartTable',
    db.Column('cust_id', db.Integer, db.ForeignKey('customer.cust_id'), nullable=False),
    db.Column('prod_id', db.Integer, db.ForeignKey('product.prod_id'), nullable=False),
    db.Column('date_created', db.DateTime, nullable=False, default=datetime.utcnow())
)

class Customer(db.Model, UserMixin):
    cust_id = db.Column(db.Integer, primary_key=True)
    id = cust_id
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    cart = db.relationship(
        'Product',
        secondary = 'cartTable',
        backref = 'customer',
        lazy = 'dynamic'
    )

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def modify(self, firstname, lastname, username, email, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        db.session.commit()
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def addToCart(self, product):
        self.cart.append(product)
        db.session.commit()

class Product(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def modify(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        db.session.commit()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()