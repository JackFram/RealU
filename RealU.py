import os
import sqlite3
from functools import wraps
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
# app.config.from_object(os.environ['APP_CONFIG'])
app.config.from_object('config.DebugConfig')


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
    return render_template("index.html")


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

    # return render_template("login.html", error=error)
    return os.environ['DATABASE_URL']



@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("welcome"))


if __name__ == '__main__':
    app.run()
