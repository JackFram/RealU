import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config.from_pyfile('instance/RealU_Config.py')


@app.route('/')
def hello_world():
    return '老婆大人起床了嘿嘿!'


if __name__ == '__main__':
    app.run()
