from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, Length, Email,EqualTo, ValidationError
