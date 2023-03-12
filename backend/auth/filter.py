from flask import abort
from functools import wraps
from flask_login import current_user


def level_3_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.level >= 3:
            abort(403)
        return f(*args, **kwargs)

    return decorated_function


def level_2_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.level >= 2:
            abort(403)
        return f(*args, **kwargs)

    return decorated_function
