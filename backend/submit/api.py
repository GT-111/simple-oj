import json
import datetime

from flask import request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import select

from response import Response
from database import sql
from extentions import login_manager, bcrypt
from submit.model import Submit, SubmitModel
from submit import submit_view

def get_max_id():
    max_id_submit = Submit.query.order_by(Submit.id.desc()).first()
    if max_id_submit:
        return max_id_submit.id
    else:
        return 1

def get_submit_by_id(_id: int):
    submit = sql.session.execute(select(Submit).where(Submit.id == _id))
    return submit.fetchone()[0]

# >>> judger >>> #
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5554")
# socket.send_string('test-send')

result_state = dict()
result_state[0] = 'ACCEPTED'
result_state[-1] = 'WRONG_ANSWER'
result_state[1] = 'TIME_LIMIT_EXCEEDED'
result_state[2] = 'TIME_LIMIT_EXCEEDED'
result_state[3] = 'MEMORY_LIMIT_EXCEEDED'
result_state[4] = 'RUNTIME_ERROR'
result_state[5] = 'SYSTEM_ERROR'
result_state[6] = 'COMPILE_ERROR'


@submit_view.route('/judger/code', methods=['POST'])
def require():
    content = request.get_json()
    record = get_submit_by_id(content.get('task_id'))
    return record.code


@submit_view.route('/judger/result', methods=['POST'])
def result():
    content = request.get_json()
    # data = {
    #     "task_id": task_id,
    #     "code": state_code,
    #     "detail": detail
    # }
    print(content.get('task_id'))
    print(content.get('code'))
    print(content.get('detail'))
    return 'ok'

# <<< judger <<< #


@submit_view.route('/submit', methods=['POST'])
# @login_required
def submit():
    content = request.get_json()
    r = Response()
    try:
        submit_model = SubmitModel(**content, create_time=datetime.datetime.utcnow())
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    submit_dict = submit_model.dict()
    temp_submit = Submit(**submit_dict)
    sql.session.add(temp_submit)
    sql.session.commit()
    r.status_code = 200
    r.data = temp_submit.to_json()

    # >>> message queue >>> #
    task_id = get_max_id()
    problem_id = submit_model.problem_id
    ret = "{" + "task_id: " + str(task_id) + ", problem_id: " + str(problem_id) + "}"
    socket.send_string(ret)
    # >>> message queue >>> #

    return r.to_json()


@submit_view.route('/histories')
# @login_required
def submit_histories():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    submits = Submit.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_submit.to_json_lite() for _submit in submits.items]
    return r.to_json()


@submit_view.route('/histories/user')
# @login_required
def user_submit_histories():
    _id = int(request.args.get('id'))
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    submits = sql.session.query(Submit).filter(Submit.user_id == _id)
    results = submits.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_submit.to_json_lite() for _submit in results.items]
    return r.to_json()


@submit_view.route('/histories/problem')
# @login_required
def problem_submit_histories():
    _id = int(request.args.get('id'))
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    submits = sql.session.query(Submit).filter(Submit.problem_id == _id)
    results = submits.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_submit.to_json_lite() for _submit in results.items]
    return r.to_json()


@submit_view.route('/histories/user/problem')
# @login_required
def user_problem_submit_histories():
    _user_id = int(request.args.get('user_id'))
    _problem_id = int(request.args.get('problem_id'))
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    submits = sql.session.query(Submit).filter(Submit.problem_id == _problem_id).filter(Submit.user_id == _user_id)
    results = submits.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_submit.to_json_lite() for _submit in results.items]
    return r.to_json()
