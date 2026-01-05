from database.config import db, app
from database.models import Movie
from sqlalchemy_utils import database_exists, create_database, drop_database

def reset_database():
    if database_exists(db.engine.url):
        drop_database(db.engine.url)
    create_database(db.engine.url)
    db.create_all()
    print("Database reset: all tables dropped and recreated.")

def create_movie(title, year, directors, theatre=True, MPA=None, genres=None, duration=None, rating=None):
    new_movie = Movie(
        title=title,
        year=year,
        directors=directors,
        theatre=theatre,
        MPA=MPA,
        genres=genres,
        duration=duration,
        rating=rating
    )
    db.session.add(new_movie)
    db.session.commit()
    print(f"Movie '{title}' added to the database.")

if __name__ == '__main__':

    with app.app_context():

        reset_database()  # Reset the database before adding new entries

        create_movie(title="Inception", year=2010, directors=["Christopher Nolan"], theatre=True, MPA="PG-13", genres=["Action", "Sci-Fi"], duration=148, rating=8.8),
        create_movie(title="The Godfather", year=1972, directors=["Francis Ford Coppola"], theatre=True, MPA="R", genres=["Crime", "Drama"], duration=175, rating=9.2),
        create_movie(title="The Dark Knight", year=2008, directors=["Christopher Nolan"], theatre=True, MPA="PG-13", genres=["Action", "Crime"], duration=152, rating=9.0),
        create_movie(title="Pulp Fiction", year=1994, directors=["Quentin Tarantino"], theatre=True, MPA="R", genres=["Crime", "Drama"], duration=154, rating=8.9),
        create_movie(title="Schindler's List", year=1993, directors=["Steven Spielberg"], theatre=True, MPA="R", genres=["Biography", "Drama"], duration=195, rating=9.0),
        create_movie(title="The Shawshank Redemption", year=1994, directors=["Frank Darabont"], theatre=True, MPA="R", genres=["Drama"], duration=142, rating=9.3),
        create_movie(title="Forrest Gump", year=1994, directors=["Robert Zemeckis"], theatre=True, MPA="PG-13", genres=["Drama", "Romance"], duration=142, rating=8.8),
        create_movie(title="The Matrix", year=1999, directors=["Lana Wachowski", "Lilly Wachowski"], theatre=True, MPA="R", genres=["Action", "Sci-Fi"], duration=136, rating=8.7),
        create_movie(title="Fight Club", year=1999, directors=["David Fincher"], theatre=True, MPA="R", genres=["Drama"], duration=139, rating=8.8),
        create_movie(title="Interstellar", year=2014, directors=["Christopher Nolan"], theatre=True, MPA="PG-13", genres=["Adventure", "Drama", "Sci-Fi"], duration=169, rating=8.6),
        create_movie(title="The Lord of the Rings: The Return of the King", year=2003, directors=["Peter Jackson"], theatre=True, MPA="PG-13", genres=["Adventure", "Drama", "Fantasy"], duration=201, rating=8.9),