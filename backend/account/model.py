import datetime

from flask_login import UserMixin
from mongoengine import Document, StringField, DateTimeField, BooleanField

from extentions import bcrypt


class User(UserMixin, Document):
    id = StringField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    nickname = StringField(default=username)
    password = StringField(required=True)
    email = StringField(required=True)
    create_time = DateTimeField(required=True, defalut=datetime.datetime.utcnow)
    level = StringField(required=True, default=1)
    meta = {
        'collection': 'user'
    }

    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<User %s: %r@%s>' % (self.id, self.username, self.level)

    def set_password(self, password):
        _hash = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.password = _hash
