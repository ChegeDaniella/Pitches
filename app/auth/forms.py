from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required,Email,EqualTo
from app.models import User

class SignUpForm(FlaskForm):
    username = StringField('Please enter your username', validators= [Required()])
    email = StringField('Enter your username', validators= [Required()])
    password = PasswordField('Enter password',validators=[Required(), EqualTo('password_confirm',message = 'Password must be the same')])
    password_confirm = PasswordField('Confirm password', validators = [Required()])
    submit = SubmitField('Sign Up')

def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
        raise ValidationError('There is an account with the email')

def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
        raise ValidationError('This username already exists')

class LoginForm(FlaskForm):
    email = StringField("Enter your email address",validators=[Required()])
    password = PasswordField('Enter password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
