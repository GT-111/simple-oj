import datetime

from flask_login import UserMixin

from extentions import bcrypt
from database import sql


class User(UserMixin, sql.Model):
    id = sql.Column(sql.Integer, primary_key=True)
    username = sql.Column(sql.String(100), nullable=False, unique=True)
    nickname = sql.Column(sql.String(100))
    password = sql.Column(sql.String(100))
    email = sql.Column(sql.String(100))
    level = sql.Column(sql.Integer)
    create_time = sql.Column(
        sql.DateTime,
        default=datetime.datetime.utcnow
    )

    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<User %s: %s@%s>' % (self.username, self.nickname, self.level)

    def set_password(self, password):
        _hash = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.password = _hash
