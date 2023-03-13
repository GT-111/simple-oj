from flask import abort
from functools import wraps
from flask_login import current_user


def level_required(n: int):
    def inner_func(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            if not current_user.level >= n:
                abort(403)
            return f(*args, **kwargs)

        return decorated_func

    return inner_func


def in_class_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        pass



