from flask import Flask
from werkzeug.exceptions import default_exceptions

from .core.extensions import db, migrate
from .core.utils import render_json_error
from .restaurant import restaurant_bp


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('./config_default.py')
    try:
        app.config.from_envvar('CONFIG')  # override default config
    except FileNotFoundError as e:  # CONFIG is set but file doesn't exist
        print('WARNING: %s' % e.strerror)
    except RuntimeError:  # CONFIG is not set, that's fine
        pass

    register_error_handlers(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_error_handlers(app):
    for code in default_exceptions.keys():
        app.errorhandler(code)(render_json_error)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(restaurant_bp, url_prefix='/restaurant')

