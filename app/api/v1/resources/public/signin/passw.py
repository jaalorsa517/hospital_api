from flask_restful import Resource, request
from werkzeug.security import generate_password_hash
from app.models.user import update_pass, authorized
from app.auth import token


class Passw(Resource):
    def patch(self, id):
        _token = request.get_json().get('token')
        if token is not None:
            try:
                data = token.loads(_token)
                datas = authorized(id)
                if datas:
                    if datas.get('created_on') == datas.get('update_on'):
                        if datas.get('email') == data:
                            passw = generate_password_hash(
                                request.get_json().get('new_password'))
                            if update_pass(id, passw):
                                return ({}, 204)

            except Exception as e:
                return (dict(message="Error en los datos o expiro el token"),
                        400)

        return (dict(message="La informacion estuvo errada"), 400)
