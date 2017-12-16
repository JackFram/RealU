import os
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from flask_bcrypt import Bcrypt

# create the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
from sql import *


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def hello_world():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'zhangzhihao' or request.form['password'] != 'qweasdzxc' :
            error = "Invalid username or password"
        else:
            session['logged_in'] = True
            flash("You have logged in!")
            return redirect(url_for("hello_world"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("welcome"))


if __name__ == '__main__':
    app.run()
