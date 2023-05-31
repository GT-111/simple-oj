from datetime import datetime

from pydantic import BaseModel, validator

from database import sql
from converter import sql_datetime_to_datetime


class Floor(sql.Model):
    __tablename__ = 'floor'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    title = sql.Column(
        sql.String(100)
    )
    contributor = sql.Column(
        sql.Text
    )
    create_at = sql.Column(
        sql.DateTime
    )
    description = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Floor, self).__init__(**kwargs)

    def __repr__(self):
        return '<Floor: %s>' % self.title

    def to_json(self):
        return {
            "floor": {
                "id": self.id,
                "title": self.title,
                "contributor": self.contributor,
                "create_at": sql_datetime_to_datetime(self.create_at).isoformat(),
                "description": self.description
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "contributor": self.contributor,
            "create_at": sql_datetime_to_datetime(self.create_at).isoformat(),
            "description": self.description
        }


class FloorModel(BaseModel):
    create_at: datetime
    title: str
    contributor: str
    description: str


class Comment(sql.Model):
    __tablename__ = 'comment'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    floor_id = sql.Column(
        sql.Integer
    )
    contributor = sql.Column(
        sql.Text
    )
    content = sql.Column(
        sql.Text
    )
    create_at = sql.Column(
        sql.DateTime
    )

    def to_json_lite(self):
        return {
            "id": self.id,
            "floor_id": self.floor_id,
            "contributor": self.contributor,
            "create_at": sql_datetime_to_datetime(self.create_at).isoformat(),
            "content": self.content
        }


class CommentModel(BaseModel):
    create_at: datetime
    contributor: str
    content: str
    floor_id: int








