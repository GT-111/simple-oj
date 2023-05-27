from flask import Blueprint
from flask_cors import CORS

upload_view = Blueprint('upload', __name__)
cors = CORS(upload_view)

from . import api