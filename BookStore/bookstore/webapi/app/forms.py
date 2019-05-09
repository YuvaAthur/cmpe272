from flask import Flask, render_template, request
# from flask_wtf import Form
from flask_wtf.csrf import CSRFProtect, CSRFError
from wtforms.validators import DataRequired
from wtforms import DateField, StringField, TextAreaField
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

from wtforms_components import TimeField

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# REf: http://flask.pocoo.org/docs/0.12/patterns/wtforms/ 
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

count = 0




