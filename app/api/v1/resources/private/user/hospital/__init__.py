from flask_restful import Resource, request
from app.auth import auth
from app.models.hospital import new_hospital_user


class Hospital(Resource):

    decorators = [auth.login_required]

    def post(self, id):
        nombre = request.get_json().get('nombre')
        direccion = request.get_json().get('direccion')
        servicio = request.get_json().get('servicio')

        cod = new_hospital_user(id, nombre, direccion, servicio)
        if cod:
            return (dict(message="Usuario hospital creado con el codigo {}".
                         format(cod)), 201)
        else:
            return (dict(message="No se puedo crear el recurso"), 400)
