from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from RealU import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from functools import wraps


# config
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


# helper function
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


# route
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'zhangzhihao' or request.form['password'] != 'qweasdzxc':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@users_blueprint.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash('You were logged out!')
    return redirect(url_for("welcome"))

