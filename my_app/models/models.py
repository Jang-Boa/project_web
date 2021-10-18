from enum import unique
from my_app import db

# Car Recommendation Model 
class Car(db.Model):
    __tablename__ = "Car"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False) # 자동차 이름, 제품명
    company = db.Column(db.String(32), nullable=False) # 제조사, 브랜드명 
    importation = db.Column(db.String(32), nullable=False) # 수입 여부
    types = db.Column(db.String(32), nullable=False) # 차종
    price1 = db.Column(db.Integer, nullable=False) # 최소 가격
    price2 = db.Column(db.Integer, nullable=False) # 최대 가격
    fuel_efficiency = db.Column(db.String(32), nullable=False) # 연비
    fuel = db.Column(db.String(32), nullable=False) # 차 연료 
    image = db.Column(db.String(32), nullable=False) # 차 이미지

    def __repr__(self):
        return f"""
        < 제품명: {self.name}, 
        브랜드: {self.company}, 
        차종: {self.types}, 
        가격: {self.price1} ~ {self.price2}, 
        사진: {self.image} >
        """

# User Register model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(120),unique=True, nullable=False)
