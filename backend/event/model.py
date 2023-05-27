from datetime import datetime

from pydantic import BaseModel, validator

from database import sql
from converter import sql_datetime_to_datetime


class Event(sql.Model):
    __tablename__ = 'event'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    title = sql.Column(
        sql.String(100)
    )
    contributor_id = sql.Column(
        sql.Integer
    )
    type = sql.Column(
        sql.Text
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
        super(Event, self).__init__(**kwargs)

    def __repr__(self):
        return '<Event: %s>' % self.title

    def to_json(self):
        return {
            "event": {
                "id": self.id,
                "title": self.title,
                "contributor_id": self.contributor_id,
                "type": self.type,
                "start_at": sql_datetime_to_datetime(self.start_at).isoformat(),
                "due_at": sql_datetime_to_datetime(self.due_at).isoformat(),
                "description": self.description
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "title": self.title,
            "contributor_id": self.contributor_id,
            "type": self.type,
            "start_at": sql_datetime_to_datetime(self.start_at).isoformat(),
            "due_at": sql_datetime_to_datetime(self.due_at).isoformat(),
            "description": self.description
        }


class EventModel(BaseModel):
    title: str
    contributor_id: int
    type: str
    start_at: datetime
    due_at: datetime
    description: str


class Enroll(sql.Model):
    __tablename__ = 'enroll'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    event_id = sql.Column(
        sql.Integer
    )
    user_id = sql.Column(
        sql.Integer
    )

    def __init__(self, **kwargs):
        super(Enroll, self).__init__(**kwargs)

    def to_json(self):
        return {
            "private_problem": {
                "id": self.id,
                "event_id": self.competition_id,
                "user_id": self.user_id
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "event_id": self.competition_id,
            "user_id": self.user_id
        }


class EnrollModel(BaseModel):
    event_id: int
    user_id: int


class Contains(sql.Model):
    __tablename__ = 'contains'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    serial = sql.Column(
        sql.Integer
    )
    event_id = sql.Column(
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
                "serial": self.serial,
                "event_id": self.event_id,
                "problem_id": self.problem_id
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "serial": self.serial,
            "event_id": self.event_id,
            "problem_id": self.problem_id
        }


class ContainsModel(BaseModel):
    serial: int
    event_id: int
    problem_id: int