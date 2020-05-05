from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = StringField('Enter Pitch', validators=[Required()])
    comment = StringField('Enter comments', validators=[Required()])
    Categories = SelectField('Which minute', choices=[('health','health'),('sport','Sports')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself", validators = [Required()])
    submit = SubmitField("Submit")

    

    