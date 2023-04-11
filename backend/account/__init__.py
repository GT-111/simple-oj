from flask import Blueprint
from flask_cors import CORS

account_view = Blueprint('account', __name__)
cors = CORS(account_view)

from . import api
