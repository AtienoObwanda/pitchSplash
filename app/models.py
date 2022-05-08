from flask_login import UserMixin
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(15), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'