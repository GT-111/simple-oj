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


def get_max_assignment_id():
    max_id_assignment = Event.query.filter_by(type == 'assignment').order_by(Event.id.desc()).first()
    if max_id_assignment:
        return max_id_assignment.id
    else:
        return 1


def get_max_competition_id():
    max_id_competition = Event.query.filter_by(type == 'competition').order_by(Event.id.desc()).first()
    if max_id_competition:
        return max_id_competition.id
    else:
        return 1


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


@event_view.route('/competition', methods=['POST'])
def get_competitions():
    content = request.get_json()
    r = Response()
    r.status_code = 200
    temp_events = get_competition_by_contributor_id(content.get('user_id'))
    r.data = [_event.to_json_lite() for _event in temp_events]
    return r.to_json()


@event_view.route('/assignment', methods=['POST'])
def get_assignments():
    content = request.get_json()
    r = Response()
    r.status_code = 200
    temp_events = get_assignment_by_contributor_id(content.get('user_id'))
    r.data = [_event.to_json_lite() for _event in temp_events]
    return r.to_json()


@event_view.route('/create_assignment', methods=['POST'])
def create_assignment():
    content = request.get_json()
    r = Response()
    try:
        event_model = EventModel(**content, type='assignment')
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    event_dict = event_model.dict()
    temp_assignment: Event = Event(**event_dict)
    sql.session.add(temp_assignment)
    sql.session.commit()
    temp_assignment.id = get_max_assignment_id()
    return str(temp_assignment.id)


@event_view.route('/create_competition', methods=['POST'])
def create_competition():
    content = request.get_json()
    r = Response()
    try:
        event_model = EventModel(**content, type='competition')
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    event_dict = event_model.dict()
    temp_competition: Event = Event(**event_dict)
    sql.session.add(temp_competition)
    sql.session.commit()
    temp_competition.id = get_max_competition_id()
    return str(temp_competition.id)