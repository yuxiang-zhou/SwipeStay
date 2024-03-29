from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('config')
CORS(app)
db = SQLAlchemy(app)

from app import views, models, api
