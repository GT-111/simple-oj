from flask import redirect, url_for, request, jsonify
from flask_bcrypt import generate_password_hash
from flask_login import login_required, login_user, logout_user, LoginManager

from response import Response
from database import db
from extentions import login_manager
from auth import filter
from problem.model import Problem
from ..problem import problem


@problem.route('/')
def problems_list():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    problems = Problem.objects.paginate(page=page, per_page=limit)
    r = Response()
    r.message = jsonify([_problem.to_dict() for _problem in problems.items])
    r.status_code = 200
    return r.to_json()


@problem.route('/<_id>')
def problem_detail(_id: str):
    _problem = Problem.objects.first_or_404(id=_id, activated=True)
    r = Response()
    r.message = jsonify(_problem)
    r.status_code = 200
    return r.to_json()


@problem.route('/create', method=['POST'])
@login_required
@filter.level_2_required
def create_problem():
    content = request.get_json()
    _problem = Problem(**content).save()
    r = Response()
    r.message = jsonify(_problem)
    r.status_code = 200
    return r.to_json()


@problem.route('/verify/<id>')
@login_required
@filter.level_3_required
def verify_problem(_id: str):
    _problem = Problem.objects.first_or_404(id=_id, activated=False)
    _problem.activate = True
    r = Response()
    r.message = jsonify(_problem)
    r.status_code = 200
    return r.to_json()
