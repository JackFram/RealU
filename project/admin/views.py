from flask import Blueprint, render_template
from project.sql import User, BlogPost
from project import db

admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder='templates'
)


@admin_blueprint.route('/')
def admin_home():
    users = db.session.query(User).all()
    posts = db.session.query(BlogPost).all()
    return render_template('admin_home.html', users=users, posts=posts)
