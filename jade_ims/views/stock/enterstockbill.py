from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, InputBill, Product

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


@enterstockbill.route('/stock/enter/pass')
def pass_enterstock():
    pass


@enterstockbill.route('/stock/enter/cancel')
def cancel_entersotck():
    pass
