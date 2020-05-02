from flask import render_template,redirect,url_for
from .forms import SignUpForm
from app import auth

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = SignUpForm()
    return render_template('auth/signup.html', signup_form = form)
