import datetime

from flask import request, jsonify
from flask_bcrypt import generate_password_hash
from flask_login import login_required, login_user, logout_user, LoginManager

from response import Response
from extentions import login_manager, bcrypt
from account.model import User, UserModel
from database import sql
from account import account_view


def get_by_id(_id: int):
    return User.query.filter_by(id=_id)


def get_by_name(_name: str):
    return User.query.filter_by(username=_name)


@login_manager.user_loader
def user_loader(_id: int):
    return get_by_id(_id)


@account_view.route('/information', methods=['POST'])
@login_required
def detail():
    username = request.json.get('username')
    temp_user: User = get_by_name(username)
    r = Response()
    r.status_code = 200
    r.message = jsonify(temp_user)
    r.to_response()
    return r.to_json()


@account_view.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    temp_user: User = get_by_name(username)
    r = Response()
    if temp_user is None or not bcrypt.check_password_hash(temp_user.password, password):
        r.message = 'no such user or wrong password'
        r.status_code = 401
    try:
        login_user(temp_user)
    except LoginManager.unauthorized:
        r.message = 'unauthorized user'
        r.status_code = 401
    r.message = 'user have been logged in'
    r.status_code = 200
    return r.to_json()


@account_view.route("/logout")
@login_required
def logout():
    logout_user()
    r = Response(data=None, message='user have been logged out')
    r.status_code = 200
    return r.to_json()


@account_view.route("/register", methods=['POST'])
def register():
    content = request.json()
    r = Response()
    try:
        user_model = UserModel(**content, level=1, create_time=datetime.datetime.utcnow())
        user_model.password = bcrypt.generate_password_hash(content.password)
    except ValueError:
        r.message = 'illegal arguments'
        r.status_code = 406
        return r.to_json()
    temp_user: User = User(user_model)
    sql.session.add(temp_user)
    sql.session.commit()
    r.message = 'user have been created'
    r.status_code = 200
    return r.to_json()
