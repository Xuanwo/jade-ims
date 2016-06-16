from flask import Blueprint, render_template, session, redirect, url_for
from jade_ims.models import db, Customer, InputBill, SaleBill, Stock

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
@dashboard.route('/index')
def index():
    input_data = len(InputBill.query.all())
    sale_data = len(SaleBill.query.all())
    stock_data = sum(i.Quantity for i in Stock.query.all())
    customer_data = len(Customer.query.all())
    return render_template('index.html',
                           title='仪表盘',
                           input_data=input_data,
                           sale_data=sale_data,
                           stock_data=stock_data,
                           customer_data=customer_data)
