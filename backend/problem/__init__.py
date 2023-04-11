from flask import Blueprint
from flask_cors import CORS

problem_view = Blueprint('problem', __name__)
cors = CORS(problem_view)

from . import api
