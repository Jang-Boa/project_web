# 회원가입 폼 만들기
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=3,max=25)]) # length로 길이 제한
    password1 = PasswordField('Password', validators=[DataRequired(), EqualTo('password2','비밀번호가 일치하지 않습니다.')]) # password 
    password2 = PasswordField('Check Password', validators=[DataRequired()]) # 비밀번호 확인란
    email = EmailField('Email', validators=[DataRequired(),Email()]) # 이메일 
