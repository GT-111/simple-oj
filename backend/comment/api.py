import json
from datetime import datetime

from flask import request
from flask_login import login_required, current_user
from sqlalchemy import select

from auth import filter
from response import Response
from extentions import login_manager, bcrypt
from database import sql
from account.model import User
from comment.model import Floor, FloorModel, Comment, CommentModel
from comment import comment_view

def get_max_floor_id():
    max_id_floor = Floor.query.order_by(Floor.id.desc()).first()
    if max_id_floor:
        return max_id_floor.id
    else:
        return 1


def get_max_comment_id():
    max_id_comment = Comment.query.order_by(Comment.id.desc()).first()
    if max_id_comment:
        return max_id_comment.id
    else:
        return 1


def get_details_by_id(_id: int):
    details = sql.session.execute(select(Comment).where(Floor.id == _id))
    return details


@comment_view.route('/comment')
def get_comments():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    comments = Floor.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_comment.to_json_lite() for _comment in comments.items]
    return r.to_json()


@comment_view.route('/create_floor', methods=['POST'])
def create_floor():
    r = Response()
    content = request.get_json()
    try:
        floor_model = FloorModel(**content)
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    floor_dict = floor_model.dict()
    temp_floor: Floor = Floor(**floor_dict)
    sql.session.add(temp_floor)
    sql.session.commit()
    temp_floor.id = get_max_floor_id()
    return str(temp_floor.id)


@comment_view.route('/create_comment', methods=['POST'])
def create_comment():
    r = Response()
    content = request.get_json()
    try:
        comment_model = CommentModel(**content)
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    comment_dict = comment_model.dict()
    temp_comment: Comment = Comment(**comment_dict)
    sql.session.add(temp_comment)
    sql.session.commit()
    temp_comment.id = get_max_floor_id()
    return str(temp_comment.id)


@comment_view.route('/details', methods=['POST'])
def get_comment_details():
    content = request.get_json()
    r = Response()
    temp_details = get_details_by_id(content.get('floor_id'))
    r.data = [_detail.to_json_lite() for _detail in temp_details]
    return r.to_json()









