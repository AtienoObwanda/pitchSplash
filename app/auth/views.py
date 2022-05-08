from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required

from .. import db,bcrypt
from .forms import RegistrationForm
from ..models import User

from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user) # add user
        db.session.commit() # commit session
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Flask Blog-Register',form=form)



