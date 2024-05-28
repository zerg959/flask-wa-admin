from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo
from blog.models import MyUser


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('admin', 'admin'), ('user', 'user')])
    submit = SubmitField('SignUp')

    def validate_username(self, username):
        user = MyUser.query.filter_by(username=username.data).first()
        if user:
            flash('This name is used already, try other', 'danger')
            raise ValidationError('Username already exists, try other name')

    def validate_email(self, email):
        user = MyUser.query.filter_by(email=email.data).first()
        if user:
            flash('This email is used already, try other', 'danger')
            raise ValidationError('Email already exists, try other address')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
