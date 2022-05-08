from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, Length, Email,EqualTo, ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(),Length(min=4, max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                    validators=[DataRequired(),Length(min=6,max=12),
                    EqualTo('confirm_password',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',
                    validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use!')


    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')