# recommend route
from flask import Blueprint, url_for, render_template

from my_app import db
from my_app.service.uploader import save_csv, insert_file

bp = Blueprint('reco', __name__, url_prefix='/recommend')

# 추천 받기 위한 페이지
@bp.route('/prefer/')
def recommend():
    save_csv(2) # 2 페이지 크롤링 
    insert_file() # 
    return render_template('reco/prefer.html')

# 추천 결과 페이지
@bp.route('/results/')
def result():
    return render_template('reco/results.html')