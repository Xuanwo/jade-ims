import views
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from jade_ims.views.home import home
from jade_ims.views.install import install

app.register_blueprint(home)
app.register_blueprint(install)

db = SQLAlchemy(app)
db.init_app(app)
