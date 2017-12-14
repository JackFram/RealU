import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
# app.config.from_object(os.environ['APP_CONFIG'])
app.config.from_object('config.DebugConfig')

@app.route('/')
def hello_world():
    return render_template("base.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'zhangzhihao' or request.form['password'] != 'qweasdzxc' :
            error = "Invalid username or password"
        else:
            flash("You have logged in!")
            return redirect(url_for("hello_world"))
    return render_template("login.html", error=error)

if __name__ == '__main__':
    app.run()
