from flask import Blueprint, render_template

stock = Blueprint('stock', __name__)

@stock.route('/stock')
@stock.route('/stock/stock')
def list_stock():
    return render_template('stock/stock.html')