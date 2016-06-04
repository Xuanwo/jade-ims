from flask import Blueprint, render_template
from jade_ims.models import db, User

dashboard = Blueprint('home', __name__)


@dashboard.route('/')
@dashboard.route('/index')
def index():
    return render_template('index.html')


@dashboard.route('/login')
def login():
    return 'Hello,world!'


@dashboard.route('/logout')
def logout():
    pass
