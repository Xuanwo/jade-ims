from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, InputBill, Product, Stock

enterstockbill = Blueprint('enterstockbill', __name__)


@enterstockbill.route('/stock/enter')
def list_enterstock():
    data = []
    inputbill_data = InputBill.query.all()
    for i in inputbill_data:
        data.append(
            {
                "ID": i.ID,
                "Product_Name": Product.query.get(i.Product_ID).Name,
                "Quantity": i.Quantity,
                "Price": i.Price,
                "DateTime": i.DateTime,
                "Remark": i.Remark
            }
        )
    return render_template('stock/enterstockbill.html',
                           data=data)


@enterstockbill.route('/stock/enter/pass', methods=['POST'])
def pass_enterstock():
    form = request.form
    print(form)
    inputbill = InputBill.query.get(int(form['inputbillid']))
    stock = Stock.query.get(int(inputbill.Product_ID))
    stock.Quantity += inputbill.Quantity
    if request.method == 'POST':
        try:
            db.session.add(stock)
            db.session.delete(inputbill)
            db.session.commit()
            flash('进货单审核成功！', 'success')
        except:
            db.session.rollback()
            flash('进货单审核失败，请重试！', 'danger')
    return redirect(url_for('enterstockbill.list_enterstock'))


@enterstockbill.route('/stock/enter/cancel', methods=['POST'])
def cancel_entersotck():
    form = request.form
    print(form)
    inputbill = InputBill.query.get(int(form['inputbillid']))
    if request.method == 'POST':
        db.session.delete(inputbill)
        db.session.commit()
        flash('进货单取消成功！', 'success')
    return redirect(url_for('enterstockbill.list_enterstock'))
