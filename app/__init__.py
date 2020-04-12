from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

# Define WSGI app object
app = Flask(__name__)
uri = os.environ['DATABASE_URL']

engine = create_engine(uri)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# create db file using SQLAlchemy
db.create_all()
migrate = Migrate(app, db)
