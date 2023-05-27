import json
from datetime import datetime

from flask import request
from flask_login import login_required, current_user
from sqlalchemy import select

from auth import filter
from response import Response
from extentions import login_manager, bcrypt
from database import sql
from account.model import User
from event.model import Event, EventModel, Enroll, EnrollModel, Contains, ContainsModel
from event import event_view


def get_event_by_id(_id: int):
    event = sql.session.execute(select(Event).where(Event.id == _id))
    return event.fetchone()[0]


def get_competition_by_contributor_id(_id: int):
    competition = sql.session.execute(select(Event).where(Event.contributor_id == _id and Event.type == 'competition'))
    return competition.fetchall()


def get_assignment_by_contributor_id(_id: int):
    assignment = sql.session.execute(select(Event).where(Event.contributor_id == _id and Event.type == 'assignment'))
    return assignment.fetchall()


def get_competition_enroll_by_id(_id: int):
    enrolls = sql.session.execute(select(Enroll).where(Enroll.user_id == _id))
    # for enroll in enrolls.fetchall():
    return 0

def get_assignment_enroll_by_id(_id: int):
    return 0


