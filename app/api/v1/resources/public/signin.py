from flask_restful import Resource, request
from app.utils import get_password_random
from app.models.user import signin_insert


class Signin(Resource):
    def post(self):
        id = request.get_json().get('id')
        email = request.get_json().get('email')
        telefono = request.get_json().get('telefono')
        contraseña = get_password_random()
        resp = signin_insert(id, email, telefono, contraseña)
        return ({
            "message": "Revise el correo brindado para la contraseña"
        }, 201) if resp else ({
            "message": "Resource not created"
        }, 400, {
            "code": 400
        })
