from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'movies'
DB_PASSWORD = 'secret'
DB_USERNAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5433'

app = Flask(__name__, template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)