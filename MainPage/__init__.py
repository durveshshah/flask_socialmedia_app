import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
#Secret Key from Python Interpretor to generate random secret key
# import secrets
# secrets.token_hex(length) here we took length as 16
app.config['SECRET_KEY'] = 	'98b38ea83f0d5b2cb2f30bccc9ae4032'
#setting up database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db' 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from MainPage import routes
