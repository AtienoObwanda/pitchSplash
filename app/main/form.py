from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import SelectField,TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, Length, Email,EqualTo, ValidationError




class PostForm(FlaskForm):

    content = TextAreaField('Content',validators=[DataRequired()])

    category = SelectField('Category', choices=[('General', 'General'),('Fun','Fun'),('Career','Career')],validators=[DataRequired()])

    submit = SubmitField('Splash Pitch')
