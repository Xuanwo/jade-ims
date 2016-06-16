from flask import Flask, session, render_template, redirect, url_for, request
from jade_ims.models import db
from werkzeug.utils import import_string

bps = ['jade_ims.views.dashboard:dashboard',
       'jade_ims.views.install:install',
       'jade_ims.views.login:login',
       'jade_ims.views.sale:sale',
       'jade_ims.views.customer:customer',
       'jade_ims.views.purchase.inputbill:inputbill',
       'jade_ims.views.purchase.supplier:supplier',
       'jade_ims.views.stock.enterstockbill:enterstockbill',
       'jade_ims.views.stock.leavestockbill:leavestockbill',
       'jade_ims.views.stock.stock:stock'
       ]


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    @app.before_request
    def check_need_login():
        if 'logged_in' not in session and request.endpoint not in ('login.user_login', 'static'):
            return redirect(url_for('login.user_login'))

    db.init_app(app)

    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)

    return app
