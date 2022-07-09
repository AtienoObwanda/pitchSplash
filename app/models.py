from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#User Model

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    pitches = db.relationship('Pitch', backref='author',lazy=True) #defining the one to many relationship btn pitch and author
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    likes =  db.relationship('Like',backref='user',lazy='dynamic')
    dislikes =  db.relationship('Dislike',backref='user',lazy='dynamic')

    # def get_reset_token(self, expires_sec=3600): # Requested link expires in one hour
    #     return s.dumps({'user_id':self.id}).decode('utf8')

    # @staticmethod
    # def verify_reset_token(token): # validate token
    #     s= Serializer(app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)



    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'


# Pitch

class Pitch (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    datePosted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the post author
    comment =  db.relationship('Comment',backref='pitch',lazy='dynamic')
    likes =  db.relationship('Like',backref='pitch',lazy='dynamic')
    dislikes =  db.relationship('Dislike',backref='pitch',lazy='dynamic')



def __repr__(self):
    return f"User({self.content},{self.datePosted})"


# Comment
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
    comment = db.Column(db.String(100))




def __repr__(self):
    return f'User({self.comment})'


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
   

class Dislike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
   