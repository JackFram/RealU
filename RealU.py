import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__, instance_path="/Users/zhangzhihao/Documents/RealU/instance", instance_relative_config=True)
app.config.from_pyfile('RealU_Config.py')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
