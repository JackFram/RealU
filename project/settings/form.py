from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class EditProfileForm(FlaskForm):
    about_me = StringField(
        'about_me',
        validators=[DataRequired(), Length(max=60)]
    )


class AvatarForm(FlaskForm):
    file = FileField('上传图片：')
    name = StringField('真实姓名：')
    submit = SubmitField('提交')


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

