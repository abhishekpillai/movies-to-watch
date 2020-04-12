from flask import Flask
from app.config import DATABASE_URI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

# Define WSGI app object
app = Flask(__name__)
uri = os.environ['DATABASE_URI'] or DATABASE_URI

engine = create_engine(DATABASE_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)
# create db file using SQLAlchemy
db.create_all()
migrate = Migrate(app, db)
