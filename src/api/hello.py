from src.api import api
import flask_restplus as _fr
from src.model import db
from src.model.user import User


@api.route('/getall', methods=['GET'])
class Hello(_fr.Resource):
    def get(self):
        users = User.query.get_all()
        rs = [u.name for u in users]
        return rs
