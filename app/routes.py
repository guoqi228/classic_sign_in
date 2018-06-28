from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import SigninFormEmail, SigninFormPassword, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, load_user
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('signin_email'))
    return render_template('index.html', title='Home Page')

@app.route('/signin_email', methods = ['GET', 'POST'])
def signin_email():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signin_form_email = SigninFormEmail()
    if signin_form_email.validate_on_submit():
        user_email = User.query.filter_by(email=signin_form_email.useremail.data).first()
        # session['useremail'] = useremail
        if user_email is None:
            flash('* Email does not exist!')
            return redirect(url_for('signin_email'))
        return redirect(url_for('signin_password', email=signin_form_email.useremail.data))
    return render_template('signin_email.html', form = signin_form_email)

@app.route('/signin_password/<email>', methods = ['GET', 'POST'])
def signin_password(email):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signin_form_password = SigninFormPassword()
    if signin_form_password.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(signin_form_password.userpassword.data):
            flash('* Password does not match!')
            return redirect('signin_email')
        login_user(user)
        flash('Thanks for signing in, {}!'.format(current_user.username))
        return redirect('index')
    return render_template('signin_password.html', form = signin_form_password)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirct('index')
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_email = User.query.filter_by(email=register_form.useremail.data).first()
        if user_email is None:
            user = User(username=register_form.username.data, email=register_form.useremail.data)
            user.set_password(register_form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('* You are now registered, please sign in.')
            return redirect('signin_email')
        else:
            flash('* Email already exists!')
            return redirect('register')
    return render_template('register.html', form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
