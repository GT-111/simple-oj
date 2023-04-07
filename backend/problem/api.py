from flask import request
from flask_login import login_required

from sqlalchemy import select
from sqlalchemy.sql.expression import text

from auth import filter
from database import sql
from problem import problem_view
from problem.model import Problem, ProblemModel
from response import Response


def get_by_id(_id: int):
    problem = sql.session.execute(select(Problem).where(Problem.id == _id))
    return problem.fetchone()[0]


def get_by_name(_name: str):
    problems = sql.session.execute(Problem.title.like('%_name%')).all()
    return problems


@problem_view.route('/')
def problems_list():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    problems = Problem.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.data = str([_problem.to_json_lite() for _problem in problems.items])
    r.status_code = 200
    return r.to_json()


@problem_view.route('/detail')
def problem_detail():
    _id = int(request.args.get('id'))
    _problem: Problem = get_by_id(_id)
    r = Response()
    r.data = _problem.to_json()
    r.status_code = 200
    return r.to_json()


@problem_view.route('/create', methods=['POST'])
# @login_required
# @filter.level_required(2)
def create_problem():
    content = request.get_json()
    r = Response()
    try:
        problem_model = ProblemModel(**content)
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    problem_dict = problem_model.dict()
    temp_problem: Problem = Problem(**problem_dict)
    sql.session.add(temp_problem)
    sql.session.commit()
    r.data = temp_problem.to_json()
    r.status_code = 200
    return r.to_json()
