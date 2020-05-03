from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class SignUpForm(FlaskForm):
    username = StringField('Please enter your username', validators= [Required()])
    email = StringField('Enter your username', validators= [Required(),Email()])
    password = PasswordField('Enter password',validators=[Required(), EqualTo('password_confirm',message = 'Password must be the same')])
    password_confirm = PasswordField('Confirm password', validators = [Required()])
    submit = SubmitField('Sign Up')

def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
        raise ValidationError('There is an account with the email')

        