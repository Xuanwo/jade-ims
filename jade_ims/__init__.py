from flask import Flask
from models import db
from werkzeug.utils import import_string

bps = ['jade_ims.views.home:home',
       'jade_ims.views.install:install'
       ]


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    db.init_app(app)

    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)

    return app
