from flask import Flask, Blueprint, render_template, request, redirect

bp = Blueprint('main',__name__, url_prefix='/') # main은 블루프린트 객체의 이름으로 나중에 함수명으로 url을 찾아주는 url_for 함수에서 사용된다. 

##### MAIN HOME PAGE #####
@bp.route('/')
def index():
    """
    Main HomePage
    """
    return render_template('index.html')
