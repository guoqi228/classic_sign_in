from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SigninFormEmail, SigninFormPassword, RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/signin_email', methods = ['GET', 'POST'])
def signin_email():
    signin_form_email = SigninFormEmail()
    if signin_form_email.validate_on_submit():
        return redirect(url_for('signin_password'))
    return render_template('signin_email.html', form = signin_form_email)

@app.route('/signin_password', methods = ['GET', 'POST'])
def signin_password():
    signin_form_password = SigninFormPassword()
    if signin_form_password.validate_on_submit():
        flash('Thank you for signing in!')
        return redirect(url_for('index'))
    return render_template('signin_password.html', form = signin_form_password)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        flash('Thank you for register!')
        return redirect(url_for('index'))
    return render_template('register.html', form=register_form)
