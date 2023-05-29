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
            "type": self.type,
            "start_at": sql_datetime_to_datetime(self.start_at).isoformat(),
            "due_at": sql_datetime_to_datetime(self.due_at).isoformat(),
            "description": self.description
        }


class EventModel(BaseModel):
    title: str
    type: str
    start_at: datetime
    due_at: datetime
    description: str


class Enrollment(sql.Model):
    __tablename__ = 'enrollment'
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
        super(Enrollment, self).__init__(**kwargs)

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


class EnrollmentModel(BaseModel):
    event_id: int
    user_id: int


class Containing(sql.Model):
    __tablename__ = 'containing'
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
        super(Containing, self).__init__(**kwargs)

    def to_json(self):
        return {
            "containing": {
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


class ContainingModel(BaseModel):
    serial: int
    event_id: int
    problem_id: int