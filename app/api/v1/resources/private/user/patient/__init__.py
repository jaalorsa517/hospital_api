from app.auth import auth
from flask_restful import Resource


class Patient(Resource):
    
    decorators=[auth.login_required]
    
    def get(self):
        return {"saludo":"hello"}