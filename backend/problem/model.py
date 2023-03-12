import datetime

from mongoengine import Document, StringField, DateTimeField, BooleanField, ListField


class Problem(Document):
    id = StringField(required=True, unique=True)
    contributor_name = StringField(required=True, unique=True)
    title = StringField(required=True)
    create_time = DateTimeField(required=True, defalut=datetime.datetime.utcnow)
    activated = BooleanField(required=True, default=False)
    type = ListField()
    meta = {
        'collection': 'problem'
    }
