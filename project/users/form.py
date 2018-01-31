from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


class RegisterForm(FlaskForm):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )
