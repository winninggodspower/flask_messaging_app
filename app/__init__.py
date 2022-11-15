from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

file_path = os.path.abspath(os.getcwd())+"\database.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = 'f6d89eb8472ebf47c276e0f40171e13e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config["USER_IMG_PATH"] = "static/profile_pics"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message_category = "info";

from app import routes, blog_routes