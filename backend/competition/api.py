import datetime

from flask import request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import select

from auth import filter
from response import Response
from extentions import login_manager, bcrypt
from database import sql
from competition.model import Competition, CompetitionModel
from competition import competition_view


def get_by_id(_id: int):
    competition = sql.session.execute(select(Competition).where(Competition.id == _id))
    return competition.fetchone()[0]

@competition_view.route('/')
def competition_list():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    competitions = Competition.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.data = str([_competition.to_json_lite() for _competition in competitions.items])
    r.status_code = 200
    return r.to_json()


@competition_view.route('/detail')
def competition_detail():
    _id = int(request.args.get('id'))
    _competition: Competition = get_by_id(_id)
    r = Response()
    r.data = _competition.to_json()
    r.status_code = 200
    return r.to_json()



@competition_view.route('/', methods=['POST'])
# @login_required
# @filter.level_required(2)
def submit():
    content = request.get_json()
    r = Response()
    try:
        competition_model = CompetitionModel(**content)
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    competition_dict = competition_model.dict()
    temp_competition: Competition = Competition(**competition_dict)
    sql.session.commit(temp_competition)
    sql.session.commit()
    r = Response()
    r.status_code = 200
    r.data = temp_competition.to_json()
    return r.to_json()


# @competition_view.route('/<id>')
# # @login_required
# # @filter.level_required(1)
# def competition_detail(id: int):
#     _competition: Competition = Competition.query.filter_by(id=id).first_of_404()
#     r = Response()
#     if _competition.start_at > datetime.datetime.utcnow():
#         r.message = jsonify(_competition)
#         r.status_code = 200
#         return r.to_json()
#     else:
#         r.status_code = 401
#         return r.to_json()
