from flask import render_template,redirect,url_for,abort
from . import main 
from .forms import PitchForm
from flask_login import login_required
from ..models import User,Pitches 
@main.route('/')

def index():
    return render_template('index.html')

@main.route('/pitch')
@login_required
def Pitche():
    form = PitchForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_pitch = Pitches(comment)
        new_pitch.save_pitch()


    return render_template('pitch.html' , pitch_form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)    

