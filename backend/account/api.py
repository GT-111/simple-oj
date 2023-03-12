from flask import redirect, url_for, request, jsonify
from flask_bcrypt import generate_password_hash
from flask_login import login_required, login_user, logout_user, LoginManager, current_user

from response import Response
from extentions import login_manager, bcrypt
from account.model import User
from ..account import account


def get_by_id(_id: str):
    return User.objects(id=_id)


def get_by_name(_name: str):
    return User.objects(username=_name)


@login_manager.user_loader
def user_loader(_id: str):
    return get_by_id(_id)


@account.route('/information', methods=['POST'])
@login_required
def detail():
    username = request.json.get('username')
    temp_user: User = get_by_name(username)
    r = Response()
    r.status_code = 200
    r.message = jsonify(temp_user)
    r.to_response()
    return r.to_json()


@account.route('/login', method=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # query user from db
    temp_user: User = get_by_name(username)
    # validating
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


@account.route("/logout")
@login_required
def logout():
    logout_user()
    r = Response(data=None, message='user have been logged out')
    r.status_code = 200
    return r.to_json()


@account.route("/register", method=['POST'])
def register():
    username = request.json.get('username')
    password = generate_password_hash(request.json.get('password'))
    email = request.json.get('email')
    r = Response()
    try:
        temp_user: User = User(username=username, password=password, email=email, type='user')
        temp_user.save()
    except ValueError:
        r.message = 'illegal arguments'
        r.status_code = 406
        r.to_response()
    r.message = 'user have been created'
    return r.to_json()