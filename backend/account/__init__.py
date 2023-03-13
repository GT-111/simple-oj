from flask import Blueprint

account_view = Blueprint('account', __name__)

from . import api
