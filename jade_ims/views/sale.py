from flask import Blueprint, render_template

sale = Blueprint('sale', __name__)

@sale.route('/sale')
def sale():
    pass