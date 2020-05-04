from flask import render_template,redirect,url_for,flash
from app.main.models import User
from .forms import SignUpForm, LoginForm
from .. import db
from . import auth
from flask_login import login_user,logout_user,login_required


@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.SignIn'))
    
    return render_template('auth/signup.html', signup_form = form)

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email =login_form.email.data).first():
        if user is not None and user.verify_password(login_form.password,data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or password')

        return render_template('auth/login.html' login_form = login_form)    

@auth.route('/logout')
@login_required
def logout():
    login_user()
    return redirect(url_for("main.index"))


    
