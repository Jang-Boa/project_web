# -*- coding: utf-8 -*- 
"""
네이버 자동차에 있는 정보를 웹 스크랩핑 하기 위한 코드입니다.
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


BASE_URL = "https://auto.naver.com/car/mainList.nhn" # BASE URL 네이버 자동차 리스트 홈페이지
IMPORT_URL = "?importYn=" # 수입 여부를 묻는 URL
PAGE_URL = "&page=" # 페이지 숫자

# BASE_URL = f"https://auto.naver.com/car" # 네이버 자동차 홈에서 자동차 리스트를 볼 수 있는 사이트의 base
# LIST_URL = f"{BASE_URL}/mainList.nhn" # 리스트 페이지 URL
# DOMESTIC_URL = f"{BASE_URL}/mainList.nhn?importYn=N&page=" # &page=2
# IMPORT_URL = f"{BASE_URL}/mainList.nhn?importYn=Y&page="

def get_page(importation='N',page_num=1):
    """
    get_page 함수는 페이지 URL 을 받아 해당 페이지를 가져오고 파싱한 두 결과들을 라턴하는 함수
    """

    page = requests.get(BASE_URL+IMPORT_URL+str(importation)+PAGE_URL+str(page_num)) # soup: BeautifulSoup 으로 파싱한 객체
    soup = BeautifulSoup(page.content,'html.parser') # page: requests 을 통해 받은 페이지 (requests 에서 사용하는 response 객체

    return soup, page

# function for get image list 
# DEFAULT INFO : 국산차, 1 페이지
def get_img(importation,page_num=1):
    """
    자동차 데이터를 수집하여 리스트 형태로 저장
    """
    if importation == 'Y':
        car_birth = '수입차' # 수입 여부 
    else:
        car_birth = '국산차'

    # img_lst = [] # 이미지 데이터를 저장할 리스트
    # lst = [] # 정보 저장할 리스트 
    names = []
    car_births =[]
    images = []
    companies =[]
    car_types = []
    car_prices_1 = []
    car_prices_2 = []
    fuel_efficiencies = []
    fuels = []

    for page in range(page_num):
        s, p = get_page(importation, page+1)
        for car in s.find_all('div',{'class':'model_ct'}):
            name = car.select('div > a > span',{'class':'box'})[0].text # 자동차 이름, 제품명
            names.append(name)

            image = car.select('div > span > a > img')[0]['src'] # 자동차의 이미지
            images.append(image)

            company = car.select('div > a > img')[0]['alt'] # 자동차 제조사, 브랜드명
            companies.append(company)

            car_type = car.select('ul > li > a > span')[0].text # 자동차의 차종
            car_types.append(car_type)
            car_price = car.select('ul > li')[0].text # 자동차 가격 (단위 : 만원)
            if car_price == '가격정보없음':
                price1 = None
                price2 = None
            else:
                price = car_price.split('\n')[2]
                price = re.sub(r'[^0-9,~]','',price)
                if '~' in price:
                    price1 = int(price.split('~')[0].replace(',',''))
                    price2 = int(price.split('~')[1].replace(',',''))
                else:
                    price1 = int(price.replace(',',''))
                    price2 = None
            car_prices_1.append(price1)
            car_prices_2.append(price2)

            fuel_efficiency = car.select('ul > li > span > span',{'class':'ell'})[0].text.strip('\n') # 연비 
            fuel_efficiencies.append(fuel_efficiency)

            fuel = car.select('ul > li > span > span',{'class':'ell'})[1].text # 연료
            f = re.sub(r'[^A-Za-z0-9가-힣,]','',fuel) # 불필요한 특수문자 제거
            fuels.append(f)
            
            car_births.append(car_birth)

            # # img_lst.append(image)
            # lst.append([name, company, car_birth, car_type, price1, price2, fuel_efficiency, f, image])
    
    cars = [data for data in zip(names,companies,car_births,car_types,car_prices_1,car_prices_2,fuel_efficiencies,fuels,images)]

    n = len(cars) # number of crawled car data
    print(f"총 {n}개의 {car_birth} 데이터를 수집하였습니다.")
    # print(cars)
    return cars