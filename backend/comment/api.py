import json
import datetime

from flask import request
from flask_login import login_required, current_user
from sqlalchemy import select

from faker import Faker

from auth import filter
from response import Response
from extentions import login_manager, bcrypt
from database import sql
from account.model import User
from comment.model import Floor, FloorModel, Comment, CommentModel
from comment import comment_view



faker = Faker()
random_name = faker.name()


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





def get_topic(_id: int):
    topic = sql.session.execute(select(Floor).where(Floor.id == _id))
    return topic.fetchone()[0]


@comment_view.route('/topic')
def get_comments():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    comments = Floor.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_comment.to_json_lite() for _comment in comments.items]
    return r.to_json()


@comment_view.route('/create_topic', methods=['POST'])
def create_floor():
    r = Response()
    content = request.get_json()
    try:
        floor_model = FloorModel(**content, create_at=datetime.datetime.utcnow())
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
        comment_model = CommentModel(**content, create_at=datetime.datetime.utcnow())
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


@comment_view.route('/detail', methods=['POST'])
def get_comment_detail():
    r = Response()
    content = request.get_json()
    temp_topic: Floor = get_topic(content.get('topic_id'))
    r.data = temp_topic.to_json()
    return r.to_json()


def get_details_by_id(_id: int):
    details = sql.session.execute(select(Comment).where(Comment.floor_id == _id))
    return details.all()


@comment_view.route('/details', methods=['POST'])
def get_comment_details():
    content = request.get_json()
    r = Response()
    temp_details = get_details_by_id(content.get('topic_id'))
    print(type(temp_details))
    for de in temp_details:
        print(type(de))
    result = []
    for detail in temp_details:
        result.append(detail[0])
        print(detail[0])
    r.data = [_detail.to_json_lite() for _detail in result]
    return r.to_json()

