from random import choice
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from string import ascii_lowercase, ascii_uppercase, digits

token = Serializer('P0R71ABC123', expires_in=3600)


def get_password_random():
    longitud = 8
    valores = ascii_uppercase + ascii_lowercase + digits

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p