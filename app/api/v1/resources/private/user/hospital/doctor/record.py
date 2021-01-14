from flask_restful import Resource, request
from app.auth import auth
from app.models.user import get_role
from app.models.record import (new_record_user, get_record_doctor,
                               get_record_hospital, get_record_patient)


class Record(Resource):
    method_decorators = {
        'get': [auth.login_required(role=['patient', 'doctor', 'hospital'])],
        'post': [auth.login_required(role='doctor')]
    }

    def get(self, id, doc):
        role = get_role(id)
        datas = None
        if role == 'patient':
            datas = get_record_patient(id)

        if role == 'doctor':
            datas = get_record_doctor(doc)

        if role == 'hospital':
            datas = get_record_hospital(id)

        if datas is not None or datas is False:
            return (dict(datas=datas), 200)
        return (dict(message='Fallo la consulta'),400)

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