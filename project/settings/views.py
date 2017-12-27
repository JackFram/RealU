from flask import Blueprint


settings_blueprint = Blueprint(
    'settings', __name__,
    template_folder='templates'
)


# route
@settings_blueprint.route('/profile')
def hello():
    return


