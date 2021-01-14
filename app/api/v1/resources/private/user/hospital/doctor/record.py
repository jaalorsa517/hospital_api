from flask_restful import Resource, request
from app.auth import auth
from app.models.record import new_record_user


class Record(Resource):
    decorators = [auth.login_required]

    def post(self, id, doc):
        paciente = request.get_json().get('paciente')
        observacion = request.get_json().get('observacion')
        estado = request.get_json().get('estado')

        cod = new_record_user(doc, paciente, observacion, estado)
        if cod:
            return (dict(message="Usuario registro creado con el codigo {}".
                         format(cod)), 201)
        else:
            return (dict(message="No se puedo crear el recurso"), 400)