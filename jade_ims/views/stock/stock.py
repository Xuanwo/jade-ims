from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, Stock, Product, Supplier

stock = Blueprint('stock', __name__)


@stock.route('/stock')
def list_stock():
    product_data = Product.query.all()
    data = []
    for i in product_data:
        data.append(
            {
                "ID": i.ID,
                "Name": i.Name,
                "Price": i.Price,
                "Supplier_Name": Supplier.query.get(i.Supplier_ID).Name,
                "Quantity": Stock.query.get(i.ID).Quantity,
                "Remark": i.Remark
            }
        )
    return render_template('stock/stock.html',
                           title="库存信息",
                           data=data)


@stock.route('/stock/add')
def add_product():
    pass


@stock.route('/stock/del')
def del_route():
    pass
