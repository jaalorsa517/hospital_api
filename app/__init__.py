from flask import Flask, current_app
from .api import api_blue

app = Flask(__name__)
app.config['SECRET_KEY'] = 'P0R71ABC123'
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(api_blue)
