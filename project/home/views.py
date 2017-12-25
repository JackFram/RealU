from project import db
from project.sql import BlogPost
from project.home.form import MessageForm
from flask import render_template, Blueprint, request, redirect, flash, url_for
from flask_login import login_required, current_user


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")
