from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_options

# Initializing extensions
db = SQLAlchemy()

def create_app(config_name):
    # Initializing app
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app