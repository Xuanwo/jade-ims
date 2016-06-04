from flask import Blueprint, render_template
from jade_ims.models import db, User

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
@dashboard.route('/index')
def index():
    return render_template('index.html', page_header='仪表盘')

