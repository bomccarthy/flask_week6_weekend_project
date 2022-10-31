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
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    category = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, name, price, description, category, image, rating, ratings_count):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.image = image
        self.rating = rating
        self.ratings_count = ratings_count

    def modify(self, name, price, description, category, image, rating, ratings_count):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.image = image
        self.rating = rating
        self.ratings_count = ratings_count
        db.session.commit()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()