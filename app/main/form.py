from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, ValidationError
from flask_login import current_user




class PitchForm(FlaskForm):

    content = TextAreaField('Content',validators=[DataRequired()])

    category = SelectField('Category', choices=[('General', 'General'),('Fun','Fun'),('Career','Career')],validators=[DataRequired()])

    submit = SubmitField('Splash Pitch')
