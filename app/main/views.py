from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .forms import PitchForm, CommentForm
from . import main
from ..models import Dislike, Pitch, Comment, Like
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

@main.route('/general')
def general():
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='General').all()
    return render_template('general.html', pitch=pitch, title='General Pitches', pitches=pitches)


@main.route('/fun')
def fun():
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='Fun').all()
    return render_template('fun.html', pitch=pitch, title='Fun Pitches', pitches=pitches)

@main.route('/career')
def career():
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='Career').all()
    return render_template('career.html', pitch=pitch, title='Career Pitches', pitches=pitches)


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


@main.route('/like/<pitch_id>/',methods = ['GET'])
@login_required
def like(pitch_id):
    pitch = Pitch.query.filter_by(id=pitch_id)
    like = Like.query.filter_by(author= current_user.id, pitch_id=pitch_id).first()
    dislike = Dislike.query.filter_by(author= current_user.id, pitch_id=pitch_id).first()

    if not pitch:
        flash('Pitch not found',category='error')
    elif like:
        return redirect(url_for('main.index', pitch_id=pitch_id))
    else:
        db.session.delete(dislike)
        like= Like(author=current_user.id, pitch_id=pitch_id)
        db.session.add(like)
        db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/dislike/<pitch_id>/',methods = ['GET'])
@login_required
def dislike(pitch_id):
    pitch = Pitch.query.filter_by(id=pitch_id)
    dislike = Dislike.query.filter_by(author= current_user.id, pitch_id=pitch_id).first()
    like = Like.query.filter_by(author= current_user.id, pitch_id=pitch_id).first()

    if not pitch:
        flash('Pitch not found',category='error')
    elif dislike:
        return redirect(url_for('main.index', pitch_id=pitch_id))
    else:
        db.session.delete(like)
        dislike= Dislike(author=current_user.id, pitch_id=pitch_id)
        db.session.add(dislike)
        db.session.commit()

    return redirect(url_for('main.index'))


# Delete comment
@main.route('/delete/comment/<comment_id>')
@login_required

def deleteComment(comment_id):
    comment = Comment.query.filter(Comment.id == comment_id).first()

    if not comment:
        flash('Comment not found', category='error')
    elif current_user.id != comment.user.id and  current_user.id != pitch.author.id:
        flash('YOu are not authorized to delete this comment', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('main.index'))

