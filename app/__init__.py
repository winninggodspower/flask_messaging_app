from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = 'f6d89eb8472ebf47c276e0f40171e13e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
app.config["USER_IMG_PATH"] = "static/profile_pics"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message_category = "info";

from app import routes, blog_routes