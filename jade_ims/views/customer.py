from flask import Blueprint, render_template

customer = Blueprint('customer', __name__)


@customer.route('/customer')
def list_user():
    return render_template('customer.html')


@customer.route('/customer/add')
def add_user():
    pass


@customer.route('/customer/del')
def del_user():
    pass
