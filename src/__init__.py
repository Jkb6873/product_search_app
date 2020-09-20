from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.controller import api
from .encoder import CustomEncoder
from .data import db
from .data.populate import populate_db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.json_encoder = CustomEncoder
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    populate_db(app)
    return app
