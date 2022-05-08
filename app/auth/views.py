from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required

from .. import db,bcrypt
from .forms import RegistrationForm, LoginForm
from ..models import User

from . import auth


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
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", title='Flask Blog-Register',form=form)



@auth.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next') #  when user tries to acccess restricted page
            return redirect(next_page) if next_page else redirect(url_for('main.index')) # redirects to requested page after loggin in if it exists... if none, redirects to home page
        else:
            flash('Login Failed. Kindly check your email and password then try again','danger')
    return render_template("auth/login.html",form=form,title='Flask Blog-Login')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
