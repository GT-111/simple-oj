from flask import Blueprint

enroll_view = Blueprint('enroll', __name__)

from . import api