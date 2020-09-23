from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
loginManager = LoginManager()
loginManager.login_view = 'users.login'
loginManager.login_message_category = 'info'

#mail goes here

def createApp(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    db.init_app(app)
    bcrypt.init_app(app)
    loginManager.init_app(app)

    return app
