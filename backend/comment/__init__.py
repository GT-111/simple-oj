from flask import Blueprint
from flask_cors import CORS

comment_view = Blueprint('comment', __name__)
cors = CORS(comment_view)

from . import api