from flask import Blueprint

api_blue = Blueprint("api", "__name__", url_prefix="/api/v1")

from .v1 import api