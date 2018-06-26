from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class SigninFormEmail(FlaskForm):
    useremail = StringField('Email (Phone for mobile account)', validators=[DataRequired(), Email()])
    submit = SubmitField('Continue')

class SigninFormPassword(FlaskForm):
    userpassword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    useremail = StringField('Email', validators=[DataRequired(), Email(), EqualTo('re_useremail', message='*Email do not match')])
    re_useremail = StringField('Re-enter Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('re_password', message='*Password do not match')])
    re_password = PasswordField('Re-enter Password', validators=[DataRequired()])
    submit = SubmitField('Register')
