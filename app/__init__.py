from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, Customer, Product
from flask_login import LoginManager, login_manager

from app.auth.routes import auth
from app.shop.routes import shop

apps = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(cust_id):
    return Customer.query.get(cust_id)

apps.config.from_object(Config)

# registering your blueprint
apps.register_blueprint(auth)
apps.register_blueprint(shop)

# initialize our database to work with our app
db.init_app(apps)
migrate = Migrate(apps, db)
login.init_app(apps)

from . import routes
from . import models