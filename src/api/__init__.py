import flask_restplus as _fr
from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = _fr.Api(
    app=api_blueprint
)


def init_api(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    app.register_blueprint(api_blueprint)


from . import hello
