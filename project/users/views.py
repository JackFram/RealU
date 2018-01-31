from flask import flash, redirect, render_template, request, \
     url_for, Blueprint, session
from project.users.form import LoginForm, RegisterForm
from project import db
from project.sql import User, bcrypt
from flask_login import login_user, login_required, logout_user, current_user
from project.token import generate_confirmation_token, confirm_token
import datetime
from project.email import send_email
from werkzeug.urls import url_parse

# config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


# route
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.user_homepage', username=current_user.name))
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user, remember=form.remember_me.data)
                session['admin'] = user.admin
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('users.user_homepage', username=user.name)
                return redirect(next_page)
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were logged out!')
    session.pop('admin', None)
    return redirect(url_for("home.home"))


@users_blueprint.route('/register', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is not None:
            error = "This email has already been registered. Please use another one"
            return render_template('register.html', form=form, error=error)
        if User.query.filter_by(name=form.username.data).first() is not None:
            error = "This name has already been registered. Please use another one"
            return render_template('register.html', form=form, error=error)
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data,
            confirmed=False
        )
        db.session.add(user)
        db.session.commit()

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('users.confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)
        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for('users.user_homepage', username=user.name))
    return render_template('register.html', form=form)


@users_blueprint.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('home.home'))


@users_blueprint.route("/user/<username>")
@login_required
def user_homepage(username):
    user = User.query.filter_by(name=username).first_or_404()
    return render_template("user_homepage.html", user=user)


@users_blueprint.route("/friends")
@login_required
def friends():
    friend_list = User.query.all()
    return render_template("friends.html", friend_list=friend_list)
