# recommend route
from flask import request
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.expression import func

from my_app.models.models import Car

# recommend prediction
def prediction():
    manufacturer_text = request.args.get('manufacturer')
    cartype_text = request.args.get('cartype')

    if manufacturer_text == "0" or cartype_text =='0' :
        selection = Car.query.order_by(func.random()).first()
    else:
        selection = Car.query.filter(and_(Car.company==manufacturer_text, Car.types==cartype_text)).order_by(func.random()).first_or_404()
    
    return selection