from flask_mongoalchemy import MongoAlchemy

db = MongoAlchemy()


def init_mongo(app):
    db.init_app(app)
