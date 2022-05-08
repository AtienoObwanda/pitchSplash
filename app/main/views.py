from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .forms import PitchForm, CommentForm
from . import main
from ..models import Pitch, Comment
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

@main.route('/comment/<int:pitch_id>',methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    pitch=Pitch.query.get_or_404(pitch_id)
    form = CommentForm()
    allComments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        postedComment = Comment(comment=form.comment.data,user_id = current_user.id, pitch_id = pitch_id)
        pitch_id = pitch_id
        db.session.add(postedComment)
        db.session.commit()
        flash('Comment added successfully')
        
        return redirect(url_for('main.comment',pitch_id=pitch_id))

    return render_template("comment.html",pitch=pitch, title='React to Pitch!', form = form,allComments=allComments)


@main.route('/like/<int:pitch_id>/',methods = ['GET'])
@login_required
def like(pitch_id):
    pitch = Pitch.query.filter_by(id=pitch_id)
    



@main.route('/pitch/<int:pitch_id>/unreact',methods = ['POST','GET'])
@login_required
def unreact(pitch_id):
    pass


