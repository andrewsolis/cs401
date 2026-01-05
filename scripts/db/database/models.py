from database.config import db
from dataclasses import dataclass

# Movies Model
class Movie(db.Model):

    id        = db.Column(db.Integer, primary_key=True)
    title     = db.Column(db.String(80), nullable=False)
    year      = db.Column(db.Integer, nullable=False)
    directors = db.Column(db.ARRAY(db.String), nullable=False)
    theatre   = db.Column(db.Boolean, default=True)
    MPA       = db.Column(db.String(20), nullable=True)
    genres    = db.Column(db.ARRAY(db.String), nullable=True)
    duration  = db.Column(db.Integer, nullable=True)  # Duration in minutes
    rating    = db.Column(db.Float, nullable=True)  # Average rating


    def __repr__(self):
        return f'<Movie {self.title}>'
