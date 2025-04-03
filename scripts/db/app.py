from database.models import Movie
from database.config import app, db

if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development, change to False in production