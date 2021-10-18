from flask import Flask, Blueprint, render_template, request, redirect

bp = Blueprint('main',__name__)

##### HOME PAGE #####
@bp.route('/')
def index():
    """
    Main HomePage
    """
    return render_template('index.html')
