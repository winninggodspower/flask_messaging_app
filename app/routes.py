
import os
import secrets

from flask import redirect,url_for,render_template, flash, request
from flask_login import login_user, logout_user, current_user, login_required

from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from app import db
from app import bcrypt

from app import app


def save_picture(form_picture):
    random_hex  = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, app.config.get("USER_IMG_PATH"), picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route('/',methods=['GET','POST'])
def home():
    posts = Post.query.all()[:10]
    return render_template('index.html', posts = posts, offset = 10)


@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hased_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account Created for \"{form.username.data}\" ", 'success')
        return redirect('/')
    return render_template('register.html', title='Register', form = form)

@app.route("/login", methods=['POST', "GET"])
def login():
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            flash(f"Successfully loged in as {form.email.data}", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccesful. Please check username and password", "danger")
    return render_template('login.html', title='login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    flash('successfully logged out', 'info')
    return redirect(url_for('home'))
