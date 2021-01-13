from app.models.user import authorized
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

token = Serializer('P0R71ABC123', expires_in=3600)

auth = HTTPTokenAuth('Bearer', realm="No tienes autorizacion")


@auth.verify_token
def verify_token(token_):
    try:
        data = token.loads(token_)
    except:
        return False
    if 'id' in data:
        if authorized(data.get('id')):
            return data.get('id')