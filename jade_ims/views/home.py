from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('login')
def login():
    pass


@home.route('logout')
def logout():
    pass
