# recommend route
from flask import Blueprint, url_for, render_template, request, g

from my_app import db
from my_app.service.uploader import save_csv, insert_file
from my_app.models.models import Car

bp = Blueprint('reco', __name__, url_prefix='/recommend')

# 추천 받기 위한 페이지
@bp.route('/prefer/')
def recommend():
    save_csv(2) # 2 페이지 크롤링 
    insert_file() # 
    return render_template('reco/prefer.html')

# 추천 결과 페이지
@bp.route('/results/',methods=('GET','POST'))
def result():
    if request.method == 'GET':
        manufacturer_text = request.args.get('manufacturer')
        if manufacturer_text != 0:
            select = Car.query.filter_by(company=manufacturer_text).first_or_404()
        return render_template('reco/results.html',select=select)
