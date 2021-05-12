import os

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

# include Flask class from file flask
from flask import Flask


# for the location of the current file, what is its directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create an instance of Flask class
# __name__ is a predefined setup variable
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # location of database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

login = LoginManager(app)
# right side is the function that's called to login users
login.login_view = 'login'


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'testingemailforsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'nsvgqgsycmxmfdhi'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

from app import routes, models
