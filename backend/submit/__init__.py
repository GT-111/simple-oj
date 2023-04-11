from flask import Blueprint
from flask_cors import CORS

submit_view = Blueprint('submit', __name__)
cors = CORS(submit_view)

from . import api