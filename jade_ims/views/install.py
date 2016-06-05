from flask import Blueprint, render_template, flash
from jade_ims.models import db

install = Blueprint('install', __name__)


@install.route('/install')
def check_install():
    db.create_all()
    return render_template("install.html", page_header='安装成功！')


@install.route('/remove')
def remove():
    db.drop_all()
    return 'Remove finished'
