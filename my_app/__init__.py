from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy() # 전역 변수로 db 객체 생성
migrate = Migrate() # 전역 변수로 migrate 객체 생성

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app,db)

    # BluePrint
    from .views import main_views, auth_views, reco_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(reco_views.bp)

    # import models
    from .models import models
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)