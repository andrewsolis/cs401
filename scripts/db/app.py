from database.models import Movie
from database.config import app, db
from flask import jsonify


@app.route('/', methods=['GET'])
def hello():
    return "Welcome to the Movie Database API! Use /movies to get a list of movies."

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = db.session.scalars(db.select(Movie)).all()
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development, change to False in production