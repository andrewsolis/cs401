from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import mapped_column

DB_NAME = 'movies'
DB_PASSWORD = 'secret'
DB_USERNAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '1234'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

db = SQLAlchemy(app)

# Movies Model
class Movie(db.Model):

    id        = mapped_column(db.Integer, primary_key=True)
    title     = mapped_column(db.String(80), nullable=False)
    year      = mapped_column(db.Integer, nullable=False)
    directors = mapped_column(db.ARRAY(db.String), nullable=False)
    theatre   = mapped_column(db.Boolean, default=True)
    MPA       = mapped_column(db.String(5), nullable=True)
    genres    = mapped_column(db.ARRAY(db.String), nullable=True)
    duration  = mapped_column(db.Integer, nullable=True)
    rating    = mapped_column(db.Float, nullable=True)


    def __repr__(self):
        return f'<Movie {self.title}>'

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Movie Database website!"

if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development, change to False in production