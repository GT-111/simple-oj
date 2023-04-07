from datetime import datetime

from pydantic import BaseModel, validator

from converter import sql_datetime_to_datetime
from database import sql


class Problem(sql.Model):
    __tablename__ = 'problem'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    title = sql.Column(
        sql.String(100)
    )
    contributor = sql.Column(
        sql.String(100)
    )
    start_time = sql.Column(
        sql.DateTime
    )
    time_limit = sql.Column(
        sql.Integer
    )
    content = sql.Column(
        sql.Text
    )
    status = sql.Column(
        sql.Text
    )
    tag = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Problem, self).__init__(**kwargs)

    def __repr__(self):
        return '<Problem: %s>' % self.title

    def to_json(self):
        return {
            "problem": {
                "id": self.id,
                "title": self.title,
                "contributor": self.contributor,
                "start_time": sql_datetime_to_datetime(self.start_time).isoformat(),
                "time_limit": self.time_limit,
                "content": self.content,
                "status": self.status,
                "tag": self.tag
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "contributor": self.contributor,
            "start_time": sql_datetime_to_datetime(self.start_time).isoformat(),
            "time_limit": self.time_limit,
            "content": self.content,
            "status": self.status,
            "tag": self.tag
        }


class ProblemModel(BaseModel):
    title: str
    contributor: str
    start_time: datetime
    time_limit: int
    content: str

    @validator('title')
    def title_validator(cls, name):
        if len(name) > 100 or len(name) == 0:
            raise ValueError("invalid title length")
        return name

    @validator('time_limit')
    def contributor_validator(cls, time):
        if time > 10 or time <= 0:
            raise ValueError("invalid time_limit")
        return time
