from flask import render_template
from . import auth
# # from .forms import SignUpForm
# from app import auth


@auth.route('/signup')
def signup():
    
    return render_template('auth/signup.html')
    
