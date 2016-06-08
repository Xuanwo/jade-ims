from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, Supplier
import sqlalchemy

supplier = Blueprint('supplier', __name__)


@supplier.route('/purchase/supplier')
def list_supplier():
    data = Supplier.query.all()
    return render_template('purchase/supplier.html',
                           title='供应商管理',
                           data=data)


@supplier.route('/purchase/supplier/add', methods=['POST'])
def add_supplier():
    form = request.form
    if request.method == 'POST':
        print(form)
        supplier = Supplier(form['supplier_name'],
                            form['supplier_constract'],
                            form['supplier_phone'],
                            form['supplier_address'],
                            form['supplier_remark'])
        try:
            db.session.add(supplier)
            db.session.commit()
            flash('供应商添加成功！', 'success')
        except:
            db.session.rollback()
            flash('输入不合法，请重新输入！', 'danger')
    return redirect(url_for('supplier.list_supplier'))


@supplier.route('/purchase/supplier/del', methods=['POST'])
def del_supplier():
    data = request.json
    print(data)
    if request.method == 'POST':
        for i in data['checked']:
            print(i)
            db.session.delete(Supplier.query.get(int(i)))
            db.session.commit()
        flash('供应商删除成功！', 'success')
    return redirect(url_for('supplier.list_supplier'))
