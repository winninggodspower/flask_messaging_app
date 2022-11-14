from flask_login import UserMixin
from app import db, login_manager
from datetime import datetime

@login_manager.user_loader
def user_loader(user_id):
    #TODO change here
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String,
                         nullable=False,
                         unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    image_file = db.Column(db.String(),
                        nullable = False,
                        default = "default.jpeg")
    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(50), 
                nullable=False)
    text = db.Column(db.String(500),
                nullable=False)
    date_posted = db.Column(db.DateTime,
                nullable = False,
                default = datetime.now)
                
    user_id = db.Column(db.Integer,
                db.ForeignKey('users.id'),
                nullable = False)
