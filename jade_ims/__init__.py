from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views.home import home
from models import User

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.register_blueprint(home)

db = SQLAlchemy(app)
db.init_app(app)


@app.route('/install')
def install():
    db.create_all()
    return 'Install finished'


@app.route('/remove')
def remove():
    db.drop_all()
    return 'Remove finished'


@app.route('/add')
def add():
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return User.query.all()
