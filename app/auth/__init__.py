from app.models.user import authorized, get_role
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

token = Serializer('P0R71ABC123', expires_in=3600)

auth = HTTPTokenAuth('Bearer', realm="No tienes autorizacion")


@auth.get_user_roles
def get_user_roles(user):
    return get_role(user)


@auth.verify_token
def verify_token(token_):
    try:
        data = token.loads(token_)
    except:
        return False
    if 'id' in data:
        if authorized(data.get('id')):
            return data.get('id')