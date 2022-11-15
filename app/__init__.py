from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_migrate import Migrate

mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
# 匿名用户访问保护页面时候，重定向到此页面
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # prefix随便写，无耦合

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .webOWL import webOWL as webOWL_blueprint
    app.register_blueprint(webOWL_blueprint, url_prefix='/view')

    from .upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint, url_prefix='/upload')

    from .moderator import moderator as moderator_blueprint
    app.register_blueprint(moderator_blueprint, url_prefix='/moderator')

    from .modify import modify as modify_bluepoint
    app.register_blueprint(modify_bluepoint, url_prefix='/modify')

    from .recommend import recommend as recommend_bluepoint
    app.register_blueprint(recommend_bluepoint, url_prefix='/recommend')
    return app


