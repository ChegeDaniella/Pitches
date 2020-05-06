from flask import render_template,redirect,url_for,flash,request
from app.models import User
from .forms import SignUpForm, LoginForm, validate_email
from .. import db
from . import auth
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from wtforms import ValidationError


@auth.route('/sign_up', methods = ["GET","POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # import pdb; pdb.set_trace()
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
    
        if User.query.filter_by(email = form.email.data).first():
            
            return redirect(url_for('auth.signup'))
            # redirect(url_for('auth.login'))

            db.session.add(user)
            db.session.commit()

        mail_message("Welcome to 1 minute","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        
        title = "Create an Acccount"
    return render_template('auth/sign_up.html', signup_form = form)

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email =login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    return render_template('auth/login.html' ,login_form = login_form)    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


    
