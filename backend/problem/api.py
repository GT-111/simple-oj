from flask import request, jsonify
from flask_login import login_required

from auth import filter
from database import sql
from problem import problem_view
from problem.model import Problem
from response import Response


def get_by_id(_id: int):
    return Problem.query.filter_by(id=_id)


@problem_view.route('/')
def problems_list():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    problems = Problem.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.message = jsonify([_problem.to_dict() for _problem in problems.items])
    r.status_code = 200
    return r.to_json()


@problem_view.route('/<_id>')
def problem_detail(id: int):
    _problem: Problem = Problem.query.filter_by(id=id).first_or_404()
    r = Response()
    if _problem.competition_id != id:
        r.message = jsonify(_problem)
        r.status_code = 200
        return r.to_json()
    else:
        r.status_code = 404
        return r.to_json()


@problem_view.route('/create', methods=['POST'])
@login_required
@filter.level_required(2)
def create_problem():
    content = request.get_json()
    _problem = Problem(**content)
    sql.session.add(_problem)
    sql.session.commit()
    r = Response()
    r.message = jsonify(_problem)
    r.status_code = 200
    return r.to_json()
