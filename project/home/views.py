from project import db
from project.sql import BlogPost
from functools import wraps
from flask import session, redirect, url_for, render_template, flash, Blueprint


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")


