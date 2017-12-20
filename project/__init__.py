#################
#    imports    #
#################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_mail import Mail

################
#    config    #
################

app = Flask(__name__)
bcrypt = Bcrypt(app)
LoginManager.login_view = "users.register"
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
mail = Mail(app)


from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.admin.views import admin_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


from project.sql import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
