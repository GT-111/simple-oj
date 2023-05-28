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


def get_details_by_id(_id: int):
    details = sql.session.execute(select(Floor).where(Floor.id == _id))
    return details


@comment_view.route('/')
def get_comments():
    _page = int(request.args.get('page', 1))
    _per_page = int(request.args.get('limit', 10))
    comments = Floor.query.paginate(page=_page, per_page=_per_page)
    r = Response()
    r.status_code = 200
    r.data = [_comment.to_json_lite() for _comment in comments.items]
    return r.to_json()


@comment_view.route('/detail')
def get_comment_detail():
    content = request.get_json()
    temp_details = get_details_by_id(content.get(''))
    r = Response()








