from flask_restful import Resource, request
from app.auth import auth
from app.models.doctor import new_doctor_user


class Doctor(Resource):
    decorators = [auth.login_required(role=['hospital', 'doctor'])]

    def post(self, id):
        especialidad = request.get_json().get('especialidad')

        cod = new_doctor_user(especialidad)
        if cod:
            return (dict(
                message="Usuario doctor creado con el codigo {}".format(cod)),
                    201)
        else:
            return (dict(message="No se puedo crear el recurso"), 400)