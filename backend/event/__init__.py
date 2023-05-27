from flask import Blueprint
from flask_cors import CORS

event_view = Blueprint('event', __name__)
cors = CORS(event_view)

from . import api