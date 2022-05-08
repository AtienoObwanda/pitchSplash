from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Defining likes:
likes = db.Table('likes',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('pitch_id', db.Integer, db.ForeignKey('pitch.id'))
                 )



#User Model

class User(UserMixin, db.Model):

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(15), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(120), nullable=False, default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    pitches = db.relationship('Pitch', backref='author',lazy=True) #defining the one to many relationship btn pitch and author
    comment = db.relationship('Comment', backref='user', lazy='dynamic')


    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'


# Pitch

class Pitch (db.Model):

    id=db.Column(db.Integer, primary_key=True)
    datePosted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the post author
    comment =  db.relationship('Comment',backref='pitch',lazy='dynamic')

def __repr__(self):
    return f"User({self.content},{self.datePosted})"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
    comment = db.Column(db.String(100))

def __repr__(self):
    return f'User({self.comment})'
