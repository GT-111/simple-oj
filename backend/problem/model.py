import datetime

from database import sql


class Problem(sql.Model):
    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(100))
    contributor = sql.Column(sql.String(100))
    create_time = sql.Column(sql.DateTime)
    due_time = sql.Column(sql.DateTime)
    time_limit = sql.Column(sql.Integer)
    total_submit = sql.Column(sql.Integer, default=0)
    ac = sql.Column(sql.Integer, default=0)
    re = sql.Column(sql.Integer, default=0)
    ce = sql.Column(sql.Integer, default=0)
    tle = sql.Column(sql.Integer, default=0)
    content = sql.Column(sql.Text)
    competition_id = sql.Column(sql.Integer)

    def __repr__(self):
        return '<Problem: %s>' % self.title
