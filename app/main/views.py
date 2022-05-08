from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .form import PitchForm
from . import main
from ..models import Pitch
from .. import db


# Views
@main.route('/')
@main.route('/home')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    return render_template('index.html', pitches=pitches, title='Pitch Splash-Just Pitch it!')


@main.route('/pitch/new',methods=['GET', 'POST'])
@login_required
def pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch=Pitch(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Pitch added successfully!','success')
        return redirect(url_for('main.index'))
    return render_template("pitch.html", title='Pitch-Splash | New Pitch', form=form)

