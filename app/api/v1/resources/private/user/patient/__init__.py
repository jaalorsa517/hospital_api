from app.auth import auth
from flask_restful import Resource, request
from app.models.patient import new_patient_user


class Patient(Resource):

    decorators = [auth.login_required]

    def post(self, id):
        nombre = request.get_json().get('nombre')
        direccion = request.get_json().get('direccion')
        nacimiento = request.get_json().get('nacimiento')

        cod = new_patient_user(id, nombre, direccion, nacimiento)
        if cod:
            return (dict(message="Usuario paciente creado con el codigo {}".
                         format(cod)), 201)
        else:
            return (dict(message="No se puedo crear el recurso"), 400)