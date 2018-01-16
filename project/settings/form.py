from flask_wtf import FlaskForm
from wtforms import FileField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class EditProfileForm(FlaskForm):
    avatar = FileField('头像')


class UpdatePasswordForm(FlaskForm):
    password = PasswordField(
        'password',
        validators=[
            DataRequired(), Length(min=6, max=25)
        ]
    )

    confirm = PasswordField(
        'confirm',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )

    new_password = PasswordField(
        'new_password',
        validators=[
            DataRequired(), Length(min=6, max=25)
        ]
    )
