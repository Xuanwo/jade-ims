from flask import Blueprint, render_template

leavestockbill = Blueprint('leavestockbill', __name__)

@leavestockbill.route('/stock/leave')
def leave_stock():
    return render_template('stock/leavestockbill.html')