from flask import Blueprint, render_template

user = Blueprint('user', __name__)


@user.route('/user')
def list_user():
    return render_template('user.html')


@user.route('/user/add')
def add_user():
    pass


@user.route('/user/del')
def del_user():
    pass
