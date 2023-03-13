from flask import Blueprint

competition_view = Blueprint('competition', __name__)

from . import api
