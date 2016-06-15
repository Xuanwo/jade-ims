from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, InputBill, Supplier, Product

inputbill = Blueprint('inputbill', __name__)


@inputbill.route('/purchase/input')
def list_input():
    supplier_data = Supplier.query.all()
    product_data = Product.query.all()
    return render_template('purchase/inputbill.html',
                           product_data=product_data
                           )


@inputbill.route('/purchase/input/add', methods=['POST'])
def add_input():
    form = request.form
    print(form)
    return redirect(url_for('inputbill.list_input'))
