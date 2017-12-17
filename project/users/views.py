from flask import flash, redirect, render_template, request, \
     url_for, Blueprint
from project.users.form import LoginForm, RegisterForm
from project import db
from project.sql import User, bcrypt
from flask_login import login_user, login_required, logout_user
from project.token import generate_confirmation_token, confirm_token
import datetime
from project.email import send_email

# config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


# route
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                #  session['logged_in'] = True
                login_user(user)
                flash('You were logged in!')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were logged out!')
    return redirect(url_for("home.welcome"))


@users_blueprint.route('/register', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is not None:
            flash("This email has already been registered. Please use another one")
            return render_template('register.html', form=form)
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
        return redirect(url_for('home.home'))
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

