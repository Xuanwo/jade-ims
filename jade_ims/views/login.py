from flask import Blueprint, render_template, request, session, flash, redirect, url_for, g
from config import USERNAME, PASSWORD

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def user_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = '用户名不正确，请重新输入！'
        elif request.form['password'] != PASSWORD:
            error = '密码不正确，请重新输入！'
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard.index'))
    return render_template('login.html', error=error)


@login.route('/logout', methods=['GET', 'POST'])
def user_logout():
    session.pop('logged_in', None)
    return redirect(url_for('login.user_login'))
