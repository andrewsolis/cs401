from database.models import Movie
from database.config import app, db
from flask import jsonify, render_template


@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Movie Database website!"

if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development, change to False in production