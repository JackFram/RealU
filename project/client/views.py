from flask import render_template, Blueprint

client_blueprint = Blueprint(
    'client', __name__,
    template_folder='templates'
)