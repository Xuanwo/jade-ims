from flask import Blueprint, render_template

sale = Blueprint('sale', __name__)


@sale.route('/sale')
@sale.route('/sale/list')
def list():
    return render_template('sale.html')


@sale.route('/sale/add')
def add():
    pass


@sale.route('/sale/del')
def remove():
    pass


@sale.route('/sale/update')
def update():
    pass
