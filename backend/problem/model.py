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
    time_limit = sql.Column(
        sql.Integer
    )
    content = sql.Column(
        sql.Text
    )
    status = sql.Column(
        sql.Text
    )
    oss_id = sql.Column(
        sql.Integer
    )
    year = sql.Column(
        sql.Text
    )
    difficulty = sql.Column(
        sql.Text
    )
    derivation = sql.Column(
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
                "time_limit": self.time_limit,
                "content": self.content,
                "status": self.status,
                "oss_id": self.oss_id,
                "year": self.year,
                "difficulty": self.difficulty,
                "derivation": self.derivation
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "contributor": self.contributor,
            "time_limit": self.time_limit,
            "content": self.content,
            "status": self.status,
            "oss_id": self.oss_id,
            "year": self.year,
            "difficulty": self.difficulty,
            "derivation": self.derivation
        }


class ProblemModel(BaseModel):
    title: str
    contributor: str
    time_limit: int
    content: str
    year: int
    difficulty: str
    derivation: str
