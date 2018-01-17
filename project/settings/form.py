from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class EditProfileForm(FlaskForm):
    introduction = StringField(
        'introduction',
        validators=[DataRequired(), Length(max=60)]
    )


class UpdatePasswordForm(FlaskForm):
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )

    new_password = PasswordField(
        'new_password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )

    confirm = PasswordField(
        'confirm',
        validators=[DataRequired(), EqualTo('new_password', message='Passwords must match.')]
    )
