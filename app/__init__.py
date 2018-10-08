from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['JSON_AS_ASCII'] = False
    config[config_name].init_app(app)

    db.init_app(app)

    # 附加路由和自定义的错误页面

    # 首页中的接口
    from app.operatorPage import operatorPage as operatorPage_blueprint
    app.register_blueprint(operatorPage_blueprint)

    from app.organizationPage import organizationPage as organizationPage_blueprint
    app.register_blueprint(organizationPage_blueprint)


    from app.taskPage import taskPage as taskPage_blueprint
    app.register_blueprint(taskPage_blueprint)

    from app.userPage import userPage as userPage_blueprint
    app.register_blueprint(userPage_blueprint)


    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # # 高级检索页的接口
    # from app.listPage import listPage as listPage_blueprint
    # app.register_blueprint(listPage_blueprint)


    return app

