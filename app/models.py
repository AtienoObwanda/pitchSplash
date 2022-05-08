from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#User Model

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(15), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(120), nullable=False, default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    pitches = db.relationship('Post', backref='author',lazy=True) #defining the one to many relationship btn pitch and author


    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'


# Pitch

class Pitch (db.Model):
    __tablename__ = 'pitches'
    
    id=db.Column(db.Integer, primary_key=True)
    datePosted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the post author

def __repr__(self):
    return f"User({self.content},{self.datePosted})"

