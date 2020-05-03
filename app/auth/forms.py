# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import Required,Email,EqualTo
# # from ..models import User

# class SignUpForm(FlaskForm):
#     username = StringField('Please enter your username', validators= [Required()])
#     email = StringField('Enter your username', validators= [Required(),Email()])
#     password = PasswordField('Enter password',validators=[Required(), EqualTo('password_confirm',message = 'Password must be the same')])
#     password_confirm = PasswordField('Confirm password', validators = [Required()])
#     submit = SubmitField('Sign Up')