from flask import Flask
from routes.controller import api
from util import CustomEncoder
from flask_sqlalchemy import SQLAlchemy
from data import db
from data.populate import populate_db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.json_encoder = CustomEncoder
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    db.init_app(app)
    populate_db(app)
    return app
