from flask import request, jsonify
from flask_login import login_required, current_user

from response import Response
from extentions import login_manager, bcrypt
from submit.model import Submit
from submit import submit_view


@submit_view.route('/', methods=['POST'])
@login_required
def submit():
    _user_id = request.json.data['user_id']
    _problem_id = request.json.data['problem_id']
    _code = request.files['file']
    _lang = request.json.data['lang']
    temp_submit = Submit(user_id=_user_id, problem_id=_problem_id, code=_code, lang=_lang)
    temp_submit.save()
    r = Response()
    r.status_code = 200
    r.message = jsonify(temp_submit)
    return r.to_json()


@submit_view.route('/histories')
@login_required
def submit_histories():
    _user_id = current_user['id']
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    submits = Submit.objects.paginate(page=page, per_page=limit)
    r = Response()
    r.status_code = 200
    r.message = jsonify([_submit.to_dict() for _submit in submits.items])
    return r.to_json()
