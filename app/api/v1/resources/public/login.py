from flask.json import jsonify
from flask_restful import Resource, request, url_for
from app.models.user import authorized
from werkzeug.security import check_password_hash
from app.auth import auth
from app.utils import token


class Login(Resource):
    def post(self):
        id = request.get_json().get('id')
        password = request.get_json().get('password')
        datas = authorized(id)
        if datas:

            if datas.get('created_on') == datas.get('update_on'):

                if request.get_json().get('new_password') is not None:

                    return (dict(url=url_for('api.pass', id=id),
                                 token=token.dumps(
                                     datas.get('email')).decode('utf-8')), 202)

                return (dict(message="Por favor cambie la contraseña"), 401)

            elif check_password_hash(datas.get('password', password)):

                return (dict(message="Bienvenido {}".format(auth.current_user(
                ) if auth.current_user() is not None else datas.get('email'))),
                        200)

        return (dict(message="No existes en la base de datas"), 401)
