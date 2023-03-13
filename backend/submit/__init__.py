from flask import Blueprint

submit_view = Blueprint('submit', __name__)

from . import api