# 회원가입 뷰
from flask import Blueprint, url_for, render_template, flash, request, session, g
from flask.typing import URLValuePreprocessorCallable
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from my_app import db
from my_app.service.forms import UserCreateForm, UserLoginForm
from my_app.models.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register -> Signup route function
@bp.route('/signup/',methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit(): # 이 함수는 전송된 폼 데이터의 정합성을 점검한다. 
        user = User.query.filter_by(username=form.username.data).first()
        if not user: # 사용자 아이디가 존재하지 않는 경우 회원가입이 가능하다
            user = User(username=form.username.data, 
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index')) # 폼데이터에 이상이 없을 경우 데이터베이스에 저장 후 main 페이지로 이동
        else: # 사용자 아이디가 존재하는 경우 경고 메세지 
            flash('이미 존재하는 사용자 입니다.')
    return render_template('auth/signup.html',form=form)

# Login route function
@bp.route('/login/',methods=('GET','POST'))
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user: # 사용자 아이디가 존재하지 않는 경우
            error = "존재하지 않는 사용자 입니다."
        elif not check_password_hash(user.password, form.password.data): # 비밀번호가 일치한지 판단
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index')) # 메인 홈페이지로 리디렉션
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request # 이 애너테이션이 적용된 함수는 라우트 함수보다 먼저 실행된다.
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None # g는 플라스크에서 제공하는 컨텍스트 변수이다. 이 변수는 request 변수와 마찬가지로 [요청 -> 응답] 과정에서 유효하다.
    else:
        g.user = User.query.get(user_id)

# create logout function
@bp.route('/logout/')
def logout():
    session.clear() # session 값 삭제
    return redirect(url_for('main.index')) # 메인 홈페이지로 되돌아가기 