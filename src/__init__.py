# coding = utf-8
import logging
from flask import Flask
from src.api import init_api
from src.model import init_mongo

__author__ = 'QuyPN'
_logger = logging.getLogger(__name__)


def create_app():
    import config
    app = Flask(__name__)
    app.config.from_object(config.Config)
    init_api(app)
    init_mongo(app)
    return app


app = create_app()
