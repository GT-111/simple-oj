from datetime import datetime

from pydantic import BaseModel

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


class CompetitionModel(BaseModel):
    id: int
    title: str
    contributor: str
    create_at: datetime
    start_at: datetime
    due_at: datetime
    description: str

