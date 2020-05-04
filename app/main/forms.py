from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = StringField('Enter Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself", validators = [Required()])
    submit = SubmitField("Submit")

    

    