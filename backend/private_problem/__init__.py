from flask import Blueprint

private_problem_view = Blueprint('private_problem', __name__)

from . import api