from flask import request, jsonify
from flask_login import login_required, current_user

from response import Response
from database import sql
from extentions import login_manager, bcrypt
from submit.model import Submit
from submit import submit_view


@submit_view.route('/', methods=['POST'])
@login_required
def submit():
    content = request.get_json()
    _submit = Submit(**content)
    sql.session.add(_submit)
    sql.session.commit()
    r = Response()
    r.status_code = 200
    r.message = jsonify(_submit)
    return r.to_json()


@submit_view.route('/histories')
@login_required
def submit_histories():
    _user_id = current_user['id']
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    submits = Submit.query.paginate(page=page, per_page=limit)
    r = Response()
    r.status_code = 200
    r.message = jsonify([_submit.to_dict() for _submit in submits.items])
    return r.to_json()
