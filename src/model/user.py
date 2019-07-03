from src.model import db
from flask_mongoalchemy import BaseQuery


class QueryTemplate(BaseQuery):
    def get_all(self):
        return self.all()


class User(db.Document):
    query_class = QueryTemplate
    name = db.StringField()
