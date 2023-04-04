from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# overiding email class to strip the email field for empty white space
class Email(Email):
    def __call__(self, form, field):
        field.data = field.data.strip()
        super().__call__(form, field)


class RegistrationForm(FlaskForm):
    username = StringField('username',
                validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',
                validators = [DataRequired(), Email()])
    password = PasswordField('password', 
                validators=[DataRequired(), Length(min=6)])
    comfirm_password = PasswordField('comfirm password', 
                validators=[DataRequired(), Length(min=6), EqualTo('password')]) 
    
    submit = SubmitField('Sign UP')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data.strip()).first()
        if user:
            raise ValidationError(" Email Already Taken. If Email Belongs To You Please Forward To Login")


class LoginForm(FlaskForm):
    email = StringField('Email',
                validators = [DataRequired(), Email()])
    password = PasswordField('password', 
                validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')    
    submit = SubmitField('Login')


class BlogForm(FlaskForm):
    title = StringField('Title',
                validators=[DataRequired(), Length(max=50)])
    content = TextAreaField('Content',
                validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Post')