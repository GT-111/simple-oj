from datetime import datetime

from pydantic import BaseModel, validator

from database import sql
from converter import sql_datetime_to_datetime


class Competition(sql.Model):
    __tablename__ = 'competition'
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
    create_at = sql.Column(
        sql.DateTime
    )
    start_at = sql.Column(
        sql.DateTime
    )
    due_at = sql.Column(
        sql.DateTime
    )
    description = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Competition, self).__init__(**kwargs)

    def __repr__(self):
        return '<Competition: %s>' % self.title

    def to_json(self):
        return {
            "competition": {
                "id": self.id,
                "title": self.title,
                "contributor": self.contributor,
                "create_at": sql_datetime_to_datetime(self.create_at).isoformat(),
                "start_at": sql_datetime_to_datetime(self.start_at).isoformat(),
                "due_at": sql_datetime_to_datetime(self.due_at).isoformat(),
                "description": self.description
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "contributor": self.contributor,
            "create_at": sql_datetime_to_datetime(self.create_at).isoformat(),
            "start_at": sql_datetime_to_datetime(self.start_at).isoformat(),
            "due_at": sql_datetime_to_datetime(self.due_at).isoformat(),
            "description": self.description
        }


class PrivateProblem(sql.Model):
    __tablename__ = 'private_problem'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    title = sql.Column(
        sql.String(100)
    )
    time_limit = sql.Column(
        sql.Integer
    )
    content = sql.Column(
        sql.Text
    )
    tag = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(PrivateProblem, self).__init__(**kwargs)

    def __repr__(self):
        return '<PrivateProblem: %s>' % self.title

    def to_json(self):
        return {
            "private_problem": {
                "id": self.id,
                "title": self.title,
                "time_limit": self.time_limit,
                "content": self.content,
                "tag": self.tag
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "time_limit": self.time_limit,
            "content": self.content,
            "tag": self.tag
        }


class Enroll(sql.Model):
    __tablename__ = 'enroll'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    competition_id = sql.Column(
        sql.Integer
    )
    user_id = sql.Column(
        sql.Integer
    )
    join_time = sql.Column(
        sql.DateTime
    )

    def __init__(self, **kwargs):
        super(Enroll, self).__init__(**kwargs)

    def to_json(self):
        return {
            "private_problem": {
                "id": self.id,
                "competition_id": self.competition_id,
                "user_id": self.user_id,
                "join_time": sql_datetime_to_datetime(self.join_time).isoformat()
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "competition_id": self.competition_id,
            "user_id": self.user_id,
            "join_time": sql_datetime_to_datetime(self.join_time).isoformat()
        }


class Contains(sql.Model):
    __tablename__ = 'contains'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    position = sql.Column(
        sql.String(100)
    )
    competition_id = sql.Column(
        sql.Integer
    )
    problem_id = sql.Column(
        sql.Integer
    )

    def __init__(self, **kwargs):
        super(Contains, self).__init__(**kwargs)

    def to_json(self):
        return {
            "contains": {
                "id": self.id,
                "position": self.position,
                "competition_id": self.competition_id,
                "problem_id": self.problem_id
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "position": self.position,
            "competition_id": self.competition_id,
            "problem_id": self.problem_id
        }


class CompetitionModel(BaseModel):
    id: int
    title: str
    contributor: str
    create_at: datetime
    start_at: datetime
    due_at: datetime
    description: str


class PrivateProblemModel(BaseModel):
    title: str
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


class ContainsModel(BaseModel):
    position: str
    competition_id: int
    problem_id: int