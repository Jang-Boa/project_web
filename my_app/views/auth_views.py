# 회원가입 뷰
from flask import Blueprint, url_for, render_template, flash, request
from flask.typing import URLValuePreprocessorCallable
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from my_app import db
from my_app.service.forms import UserCreateForm
from my_app.models.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/',methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit(): # 이 함수는 전송된 폼 데이터의 정합성을 점검한다. 
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, 
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index')) # 폼데이터에 이상이 없을 경우 데이터베이스에 저장 후 main 페이지로 이동
        else:
            flash('이미 존재하는 사용자 입니다.')
    return render_template('auth/signup.html',form=form)