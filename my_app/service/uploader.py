from my_app import db
from my_app.scraping.scrap import get_img
from my_app.models.models import Car
import pandas as pd
import csv 
import os

"""
database 에 크롤링한 데이터를 옮기기 위한 코드
"""
CSV_FILE_DIR = 'my_app/csv' # csv_file_dir
file_name = 'table_car.csv' # filename
# importation = 'Y' # or "N"
# page_num = 10


def save_csv(page_num):
    """
    스크래이핑한 데이터를 csv 파일로 저장하는 함수 
    """
    domestics = get_img('N',page_num) # 국산차 10페이지의 데이터 크롤링
    imports = get_img('Y',page_num) # 수입차 10 페이지의 데이터 크롤링
    # car_data = get_img(importation,page_num)

    domestics_table = pd.DataFrame(domestics,columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])
    imports_table = pd.DataFrame(imports,columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])
    # car_table = pd.DataFrame(car_data, columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])

    # car_table = pd.DataFrame(columns=['names','companies','car_births','car_types','car_prices_1','car_prices_2','fuel_efficiencies','fuels','images'])
    # car_table = car_table.append(car_data)
    table = pd.concat([domestics_table,imports_table],ignore_index=True) # concat two dataframe into one

    # domestics_table.to_csv('{}/table_domestics.csv'.format(CSV_FILE_DIR), encoding='utf-8', mode='w')
    # imports_table.to_csv('{}/table_imports.csv'.format(CSV_FILE_DIR), encoding='utf-8', mode='w')
    table.to_csv('{}/{}'.format(CSV_FILE_DIR, file_name), encoding='utf-8', mode='w')
    # car_table.to_csv('{}/{}'.format(CSV_FILE_DIR, file_name), encoding='utf-8', mode='w')
    return None

def insert_file():
    """
    csv 파일을 db 로 저장하는 함수 
    """
    with open('{}/{}'.format(CSV_FILE_DIR, file_name),encoding='utf-8') as file:
        results = []
        reader = csv.DictReader(file)
        for row in reader:
            results = Car.query.filter_by(name=row['names']).first()
            if not results: # 같은 값이 중복되어 저장되지 않도록
                results = Car(name=row['names'],
                            company=row['companies'],
                            importation=row['car_births'],
                            types=row['car_types'],
                            price1=row['car_prices_1'],
                            price2=row['car_prices_2'],
                            fuel_efficiency=row['fuel_efficiencies'],
                            fuel=row['fuels'],
                            image=row['images'])
                db.session.add(results)
                db.session.commit()
            # print('UPLOADED CSV FILE TO DB SUCCESFULLY!')

# save_csv('N',1)
# insert_file()


"""
sqlalchemy.exc.InterfaceError: (sqlite3.InterfaceError) Error binding parameter 1 - probably unsupported type.
[SQL: INSERT INTO "Car" (name, company, importation, types, price1, price2, fuel_efficiency, fuel, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('2022 캐스퍼', ['companies'], '국산차', '경형', '', '', '정보없음', '가솔린', 'https://imgauto-phinf.pstatic.net/20210901_195/auto_163045763221657AiV_PNG/20210901095324_65Cye5HC.png?type=f160_116')]
(Background on this error at: https://sqlalche.me/e/14/rvf5)
"""