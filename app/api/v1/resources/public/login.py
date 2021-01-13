from flask_restful import Resource, request, url_for
from app.models.user import authorized
from werkzeug.security import check_password_hash
from app.auth import auth, token


class Login(Resource):
    def post(self):
        id = request.get_json().get('id')
        password = request.get_json().get('password')
        datas = authorized(id)
        if datas:

            if datas.get('created_on') == datas.get('update_on'):

                return (dict(
                    message=
                    "Visite el siguiente link para poder cambiar la contraseña",
                    url=url_for('api.pass', id=id),
                    token=token.dumps(datas.get('email')).decode('utf-8')),
                        202)

            elif check_password_hash(datas.get('password'), password):

                return (dict(
                    message="Bienvenido {}".format(datas.get('email')),
                    token=token.dumps(dict(id=id)).decode('utf-8')), 200)

        return (dict(message="No existes en la base de datos"), 401)
