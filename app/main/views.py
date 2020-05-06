from flask import render_template,redirect,url_for,abort
from . import main 
from .forms import PitchForm,UpdateProfile,PlainComments
from flask_login import login_required,current_user
from app.models import User,Pitches ,Comments
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitch',methods = ['GET','POST'])
@login_required
def Pitche():
    # my_pitch = Pitch.query.get(id)
    form = PitchForm()
    comm_form = PlainComments()
    pitch = form.pitch.data
    comment = form.comment.data
    category = form.Categories.data

    if id is None:
        abort(404)

    if comm_form.validate_on_submit():
        comment_data=comm_form.comment.data
        new_comment = Commments()
        new_comment.save_comment()
    # return redirect('pitch.html')    

    if form.validate_on_submit():
        new_pitch = Pitches()
        new_pitch.save_pitch()


    return render_template('pitch.html' , pitch_form = form, comment = comment, pitch=pitch,category = category,comm_form=comm_form )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)  

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    form = UpdateProfile() 
    user = User.query.filter_by(username= uname ).first()   
    
    if user is None:
        abort(404)

    if form.validate_on_submit():
        current_user.bio = form.bio.data
        

        db.session.add(user)
        db.session.commit()
            

        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html',form = form)

   

