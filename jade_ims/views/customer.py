from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, Customer

customer = Blueprint('customer', __name__)


@customer.route('/customer')
def list_user():
    data = Customer.query.all()
    return render_template('customer.html',
                           title='客户管理',
                           data=data)


@customer.route('/customer/add', methods=['POST'])
def add_user():
    form = request.form
    if request.method == 'POST':
        print(form)
        customer = Customer(form['customer_name'],
                            form['customer_phone'],
                            form['customer_address'],
                            form['customer_remark'])
        try:
            db.session.add(customer)
            db.session.commit()
            flash('顾客添加成功！', 'success')
        except:
            db.session.rollback()
            flash('输入不合法，请重新输入！', 'danger')
    return redirect(url_for('customer.list_user'))


@customer.route('/customer/del', methods=['POST'])
def del_user():
    data = request.form.getlist('customer_check')
    if request.method == 'POST':
        for i in data:
            db.session.delete(Customer.query.get(int(i)))
            db.session.commit()
        flash('顾客删除成功！', 'success')
    return redirect(url_for('customer.list_user'))
