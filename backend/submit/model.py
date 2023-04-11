from datetime import datetime

from pydantic import BaseModel, validator

from database import sql
from converter import sql_datetime_to_datetime


class Submit(sql.Model):
    __tablename__ = 'submit'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    problem_id = sql.Column(
        sql.Integer
    )
    user_id = sql.Column(
        sql.Integer
    )
    create_time = sql.Column(
        sql.DateTime
    )
    code = sql.Column(
        sql.Text
    )
    language = sql.Column(
        sql.String(100)
    )
    status = sql.Column(
        sql.String(100)
    )
    returned = sql.Column(
        sql.Text
    )

    def __init__(self, **kwargs):
        super(Submit, self).__init__(**kwargs)

    def __repr__(self):
        return '<Submit: %s>' % self.id

    def to_json(self):
        return {
            "submit": {
                "id": self.id,
                "problem_id": self.problem_id,
                "user_id": self.user_id,
                "create_time": sql_datetime_to_datetime(self.create_time),
                "code": self.code,
                "language": self.language,
                "status": self.status,
                "returned": self.returned
            }
        }

    def to_json_lite(self):
        return {
            "id": self.id,
            "problem_id": self.problem_id,
            "user_id": self.user_id,
            "create_time": sql_datetime_to_datetime(self.create_time),
            "code": self.code,
            "language": self.language,
            "status": self.status,
            "returned": self.returned
        }


class SubmitModel(BaseModel):
    problem_id: int
    user_id: int
    create_time: datetime
    code: str
    language: str


if __name__ == '__main__':
    test = {'id': 1, 'problem_id': 1, 'user_id': 1, "create_time": "1999-01-01T23:59:59", "code": "qwer",
            "status": "1234", "language": "java", "returned": "asdf"}
    s = Submit(**test)
    print(test)
    print(s.to_json())
