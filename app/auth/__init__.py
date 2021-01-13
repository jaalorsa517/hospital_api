from werkzeug.security import check_password_hash
from app.models.user import authorized
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth('Basic',realm="No tienes autorizacion")

@auth.verify_password
def verify_password(user,passw):
    datas = authorized(user)
    if datas:
        if check_password_hash(datas.get('password'),passw):
            return user