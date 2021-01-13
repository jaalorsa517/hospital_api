from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


def get_password_random():
    longitud = 8
    valores = ascii_uppercase + ascii_lowercase + digits

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p