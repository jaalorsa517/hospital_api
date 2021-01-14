from flask_restful import Resource


class TestConnection(Resource):
    def get(self):
        return 'HELLO WORLD'