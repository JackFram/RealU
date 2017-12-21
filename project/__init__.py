#################
#    imports    #
#################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
import os
from flask_mail import Mail

################
#    config    #
################

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
mail = Mail(app)

################
#   blueprint  #
################
from project.users.views import users_blueprint
from project.home.views import home_blueprint


################
#    admin     #
################
admin_page = Admin(app, name='RealU', template_mode='bootstrap3')
from project.admin import *

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


################
#  user_login  #
################
from project.sql import User
login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
