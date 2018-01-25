from flask import Blueprint, request, render_template, flash
from project.sql import User, bcrypt
from project.settings.form import EditProfileForm, UpdatePasswordForm
from flask_login import current_user, login_required
from project import db


settings_blueprint = Blueprint(
    'settings', __name__,
    template_folder='templates'
)


# route
@login_required
@settings_blueprint.route('/profile', methods=["GET", "POST"])
def profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(name=current_user.name).first()
        user.introduction = request.form['introduction']
        db.session.commit()
        flash('更改成功!')
        return render_template("profile.html", form=form, user=current_user)
    return render_template("profile.html", form=form, user=current_user)


@login_required
@settings_blueprint.route('/setting', methods=["GET", "POST"])
def settings():
    form = UpdatePasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(name=current_user.name).first()
        if form.new_password is not None and bcrypt.check_password_hash(user.password, request.form['password']):
            user.password = bcrypt.generate_password_hash(request.form['new_password']).decode('utf-8')
            db.session.commit()
            flash("密码设置完毕!")
            return render_template("setting.html", form=form, user=current_user)
        else:
            flash("密码输入错误!")
            return render_template("setting.html", form=form, user=current_user)
    return render_template("setting.html", form=form, user=current_user)


@login_required
@settings_blueprint.route('/follow', methods=["GET", "POST"])
def follow():
    current_user.follow(current_user)
    db.session.commit()
    return "1"


