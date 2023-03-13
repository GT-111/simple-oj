from flask import Blueprint

problem_view = Blueprint('problem', __name__)

from . import api
