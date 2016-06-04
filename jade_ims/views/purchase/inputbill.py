from flask import Blueprint, render_template

inputbill = Blueprint('inputbill', __name__)


@inputbill.route('/purchase/input')
def list_input():
    return render_template('purchase/inputbill.html')
