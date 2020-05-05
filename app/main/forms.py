from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = StringField('Enter Pitch', validators=[Required()])
    Categories = SelectField('Which minute', choices=[('hlh','health'),('spt','Sports')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself", validators = [Required()])
    submit = SubmitField("Submit")

    

    