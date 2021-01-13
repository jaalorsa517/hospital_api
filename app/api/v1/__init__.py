from flask_restful import Api
from app.api import api_blue

api = Api(api_blue)

from .resources.public.login import Login
from .resources.public.signin import Signin
from .resources.private.user.patient import Patient
from .resources.private.user.hospital import Hospital
from .resources.private.user.hospital.doctor import Doctor
from .resources.private.user.hospital.doctor.record import Record

api.add_resource(Login, "/login")
api.add_resource(Signin, "/signin")
api.add_resource(Patient, "/patient")
api.add_resource(Hospital, "/Hospital")
api.add_resource(Doctor, "/Hospital/doctor")
api.add_resource(Record, "/Hospital/doctor/record")
