from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, SaleBill, Product, Stock

leavestockbill = Blueprint('leavestockbill', __name__)


@leavestockbill.route('/stock/leave')
def leave_stock():
    data = []
    salebill_data = SaleBill.query.all()
    for i in salebill_data:
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
    return render_template('stock/leavestockbill.html',
                           data=data)


@leavestockbill.route('/stock/leave/pass', methods=['POST'])
def pass_leavestock():
    form = request.form
    print(form)
    salebill = SaleBill.query.get(int(form['salebillid']))
    stock = Stock.query.get(int(salebill.Product_ID))
    if request.method == 'POST':
        if stock.Quantity >= salebill.Quantity:
            stock.Quantity -= salebill.Quantity
            try:
                db.session.add(stock)
                db.session.delete(salebill)
                db.session.commit()
                if stock.Quantity > 10:
                    flash('销货单审批成功！', 'success')
                else:
                    flash('库存即将耗尽，请及时进货！', 'warning')
            except:
                db.session.commit()
                flash('销货单审核失败，请重试！', 'danger')
        else:
            flash('库存不足，请进货！', 'danger')
    return redirect(url_for('stock.list_stock'))
