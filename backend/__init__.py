import time

from flask import Flask, g, request
from flask_cors import CORS

from account import account_view
from database import sql
from extentions import bcrypt, login_manager, mail
from problem import problem_view
from submit import submit_view
from upload import upload_view
from event import event_view
from comment import comment_view


def create_app():
    app = Flask('sandevistan')
    app.config.from_object("config.Config")

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
        for header, value in request.headers.items():
            print(header + " " + value)
        """Returns the applications index page."""
        return "don't panic"

    return app


def register_extensions(app):
    sql.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    # session.init_app(app)


def register_blueprints(app):
    app.register_blueprint(account_view, url_prefix='/account')
    app.register_blueprint(problem_view, url_prefix='/problem')
    app.register_blueprint(upload_view, url_prefix='/upload')
    app.register_blueprint(event_view, url_prefix='/event')
    app.register_blueprint(submit_view, url_prefix='/submit')
    app.register_blueprint(comment_view, url_prefix='/comment')


app = create_app()
app.run(host='0.0.0.0', port=5001)


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
