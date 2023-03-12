import datetime

from flask_login import UserMixin
from mongoengine import Document, StringField, DateTimeField, BooleanField, FileField, IntField

from extentions import bcrypt


class Submit(Document):
    id = StringField(required=True, unique=True)
    user_id = StringField(required=True)
    problem_id = StringField(required=True)
    code = FileField(required=True)
    lang = StringField(required=True)
    create_time = DateTimeField(required=True, defalut=datetime.datetime.utcnow)
    return_time = DateTimeField(required=False)
    status = IntField(required=True, default=0)
    meta = {
        'collection': 'submit'
    }