from flask import Blueprint, request, render_template, flash, url_for, redirect
from project.sql import User, bcrypt
from project.settings.form import EditProfileForm, UpdatePasswordForm, AvatarForm
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
        user.about_me = request.form['about_me']
        db.session.commit()
        flash('更改成功!')
        return render_template("profile.html", form=form)
    return render_template("profile.html", form=form)


@login_required
@settings_blueprint.route('/upload', methods=["GET", "POST"])
def upload():
    form = AvatarForm()
    if request.method == 'POST' and form.validate_on_submit():
            return str(request.files['file'].read())
    return render_template("follow.html", form=form)


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
            return render_template("setting.html", form=form)
        else:
            flash("密码输入错误!")
            return render_template("setting.html", form=form)
    return render_template("setting.html", form=form)


@settings_blueprint.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        flash('用户 {} 不存在.'.format(username))
        return redirect(url_for('users.user_homepage', username=user.name))
    if user == current_user:
        flash('你不能关注自己!')
        return redirect(url_for('users.user_homepage', username=user.name))
    current_user.follow(user)
    db.session.commit()
    flash('你关注了{}!'.format(username))
    return redirect(url_for('users.user_homepage', username=user.name))


@settings_blueprint.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        flash('用户 {} 不存在.'.format(username))
        return redirect(url_for('users.user_homepage', username=user.name))
    if user == current_user:
        flash('你不能取消关注自己!')
        return redirect(url_for('users.user_homepage', username=user.name))
    current_user.unfollow(user)
    db.session.commit()
    flash('你取消了关注{}.'.format(username))
    return redirect(url_for('users.user_homepage', username=user.name))
