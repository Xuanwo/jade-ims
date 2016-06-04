from flask import Blueprint, render_template

supplier = Blueprint('supplier', __name__)

@supplier.route('/purchase/supplier')
def list_supplier():
    return render_template('purchase/supplier.html')