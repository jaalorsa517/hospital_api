from flask import Flask
from .api import api_blue

app = Flask(__name__)
app.register_blueprint(api_blue)