import datetime

from database import sql


class Submit(sql.Model):
    id = sql.Column(sql.Integer, primary_key=True)
    problem_id = sql.Column(sql.Integer)
    create_at = sql.Column(sql.DateTime)
    status = sql.Column(sql.String(10))
    returned = sql.Column(sql.Text)
