from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# import our blueprints for registration
from .landing.routes import landing
from .auth.routes import auth

from .models import db
# import database related
from flask_migrate import Migrate

app = Flask(__name__)

from app import routes, models
app.register_blueprint(landing)
app.register_blueprint(auth)

app.config.from_object(Config)

# initialize our databse to work with our app
db.init_app(app)

migrate = Migrate(app,db)

from . import routes
from . import models
