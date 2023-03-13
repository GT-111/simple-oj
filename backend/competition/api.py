import datetime

from flask import request, jsonify
from flask_login import login_required, current_user

from auth import filter
from response import Response
from extentions import login_manager, bcrypt
from database import sql
from competition.model import Competition
from competition import competition_view


@competition_view.route('/', methods=['POST'])
@login_required
@filter.level_required(2)
def submit():
    content = request.json()
    _competition = Competition(**content)
    sql.session.commit(_competition)
    sql.session.commit()
    r = Response()
    r.status_code = 200
    r.message = jsonify(_competition)
    return r.to_json()


@competition_view.route('/<id>')
@login_required
@filter.level_required(1)
def competition_detail(id: int):
    _competition: Competition = Competition.query.filter_by(id=id).first_of_404()
    r = Response()
    if _competition.start_at > datetime.datetime.utcnow():
        r.message = jsonify(_competition)
        r.status_code = 200
        return r.to_json()
    else:
        r.status_code = 401
        return r.to_json()
