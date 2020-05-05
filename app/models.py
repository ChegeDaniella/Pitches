from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager

class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    category = db.Column(db.String(255))
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitche = Pitch.Query.filter_by(id=id).first()
        return pitche
        # Pitches.all_pitches.append(self) 


    # all_pitches = []

    # def __init__(self,comment):
    #     self.comment = comment
    #     # self.category = category

    

    # @classmethod
    # def clear_reviews(cls):
    #     Pitches.all_pitches.clear()   

    # @classmethod
    # def get_pitches(cls,id):


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cant read from this attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))      

    def __repr__(self):
        return f'User{self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref ='role',lazy ="dynamic")    

    def __repr__(self):
        return f'User {self.name}'  
        
          
