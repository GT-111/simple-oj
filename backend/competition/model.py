import datetime

from database import sql


class Competition(sql.Model):
    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(100))
    contributor = sql.Column(sql.String(100))
    create_at = sql.Column(sql.DateTime)
    start_at = sql.Column(sql.DateTime)
    due_at = sql.Column(sql.DateTime)
    description = sql.Column(sql.Text)