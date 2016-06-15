from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, Product, Customer, SaleBill
import datetime

sale = Blueprint('sale', __name__)


@sale.route('/sale')
def list_salebill():
    data = []
    product_data = Product.query.all()
    customer_data = Customer.query.all()
    salebill_data = SaleBill.query.all()
    for i in salebill_data:
        data.append(
            {
                "ID": i.ID,
                "Product_Name": Product.query.get(i.Product_ID).Name,
                "Customer_Name": Customer.query.get(i.Customer_ID).Name,
                "Price": i.Price,
                "Quantity": i.Quantity,
                "DateTime": i.DateTime,
                "Remark": i.Remark
            }
        )
    return render_template('sale.html',
                           data=data,
                           product_data=product_data,
                           customer_data=customer_data)


@sale.route('/sale/add', methods=['POST'])
def add_salebill():
    form = request.form
    if request.method == 'POST':
        print(form)
        salebill = SaleBill(
            int(Product.query.filter_by(Name=form['product_name']).first().ID),
            int(Customer.query.filter_by(Name=form['customer_name']).first().ID),
            datetime.datetime.strptime(form['datetime'], "%Y-%m-%d %H:%M"),
            int(form['salebill_number']),
            float(form['salebill_price']),
            form['salebill_remark']
        )
    try:
        db.session.add(salebill)
        db.session.commit()
        flash('销货单添加成功！', 'success')
    except:
        db.session.rollback()
        flash('输入不合法，请重新输入！', 'danger')
    return redirect(url_for('sale.list_salebill'))


@sale.route('/sale/del')
def del_salebill():
    pass
