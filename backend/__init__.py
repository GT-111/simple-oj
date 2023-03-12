import time, requests

from flask import Flask, g, render_template, request

from database import db
from extentions import bcrypt, login_manager, mail

from account import account
from problem import problem
from submit import submit


def create_app():
    """Returns an initialized Flask application."""
    app = Flask('simple-oj')
    app.config['MONGODB_SETTINGS'] = {
        'db': 'simple-oj',
        'host': 'localhost',
        'port': '27017'
    }

    register_extensions(app)
    register_blueprints(app)
    # register_errorhandlers(app)

    @app.before_request
    def before_request():
        """Prepare some things before the application handles a request."""
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index page."""
        return "don't panic"

    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(problem, url_prefix='/problem')
    app.register_blueprint(submit, url_prefix='/submit')


# def register_errorhandlers(app):
#     def render_error(e):
#         return render_template('errors/%s.html' % e.code), e.code
#
#     for e in [
#         requests.codes.INTERNAL_SERVER_ERROR,
#         requests.codes.NOT_FOUND,
#         requests.codes.UNAUTHORIZED,
#     ]:
#         app.errorhandler(e)(render_error)
