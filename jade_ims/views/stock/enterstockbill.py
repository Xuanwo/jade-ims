from flask import Blueprint, render_template

enterstockbill = Blueprint('enterstockbill', __name__)

@enterstockbill.route('/stock/enter')
def enter_stock():
    return render_template('stock/enterstockbill.html')