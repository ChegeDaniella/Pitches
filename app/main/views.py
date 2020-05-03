from flask import render_template
from . import main 
from .forms import PitchForm

# from flask_login import login_required

@main.route('/')
# @login_required
def index():
    return render_template('index.html')

@main.route('/pitch')
def Pitches():
    form = PitchForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_pitch = Pitches(comment)
        new_pitch.save_pitch()


    return render_template('pitch.html' , pitch_form = form)
