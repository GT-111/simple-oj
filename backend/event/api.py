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
from event.model import Event, EventModel, Enrollment, EnrollmentModel, Containing, ContainingModel
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


def get_competition_enrollment_by_id(_id: int):
    enrollments = sql.session.query(Enrollment).filter(Enrollment.user_id == _id)
    results = []
    for enrollment in enrollments.all():
        temp_event: Event = get_event_by_id(enrollment.event_id)
        if temp_event.type == 'competition':
            results.append(temp_event)
    return [_event.to_json_lite() for _event in results]


def get_assignment_enrollment_by_id(_id: int):
    enrollments = sql.session.query(Enrollment).filter(Enrollment.user_id == _id)
    results = []
    for enrollment in enrollments.all():
        temp_event: Event = get_event_by_id(enrollment.event_id)
        if temp_event.type == 'assignment':
            results.append(temp_event)
    return [_event.to_json_lite() for _event in results]


@event_view.route('/assignment_id', methods=['POST'])
def get_assignment_id():
    content = request.get_json()
    r = Response()
    r.status_code = 200
    r.data = get_assignment_enrollment_by_id(content.get('user_id'))
    return r.to_json()


@event_view.route('/competition_id', methods=['POST'])
def get_competition_id():
    content = request.get_json()
    r = Response()
    r.status_code = 200
    r.data = get_competition_enrollment_by_id(content.get('user_id'))
    return r.to_json()



