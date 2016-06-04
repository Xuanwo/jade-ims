from flask import Blueprint, render_template, flash
from ..models import db, User

install = Blueprint('install', __name__)


@install.route('/install')
def check_install():
    db.create_all()
    flash("Install finished")
    return render_template("install.html")


@install.route('/remove')
def remove():
    db.drop_all()
    return 'Remove finished'


@install.route('/add')
def add():
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return str(User.query.all())
