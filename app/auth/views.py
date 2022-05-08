from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required


from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')