from datetime import datetime

from pydantic import BaseModel, validator

from database import sql
from converter import sql_datetime_to_datetime


class Upload(sql.Model):
    __tablename__ = 'user_upload'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    user_id = sql.Column(
        sql.Integer
    )
    context_id = sql.Column(
        sql.Integer
    )
    oss_id = sql.Column(
        sql.Integer
    )
    grade = sql.Column(
        sql.Integer
    )
    comment = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Upload, self).__init__(**kwargs)

    def __repr__(self):
        return '<Upload: %s>' % self.id

    def to_json(self):
        return {
            "upload": {
                "id": self.id,
                "user_id": self.user_id,
                "context_id": self.context_id,
                "oss_id": self.oss_id,
                "grade": self.grade,
                "comment": self.comment
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "context_id": self.context_id,
            "oss_id": self.oss_id,
            "grade": self.grade,
            "comment": self.comment
        }


class UploadModel(BaseModel):
    user_id: int
    context_id: int
    oss_id: int


class Oss(sql.Model):
    __tablename__ = 'oss'
    id = sql.Column(
        sql.Integer,
        primary_key = True
    )
    user_id = sql.Column(
        sql.Integer
    )
    type = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Oss, self).__init__(**kwargs)

    def __repr__(self):
        return '<Upload: %s>' % self.id

    def to_json(self):
        return {
            "oss": {
                "id": self.id,
                "user_id": self.user_id,
                "type": self.type
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "type": self.type
        }

class OssModel(BaseModel):
    user_id: int
    type: str


