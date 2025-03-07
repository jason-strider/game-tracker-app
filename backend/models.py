
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    playtime = db.Column(db.Integer, default=0)
    completion_status = db.Column(db.String(20), nullable=False)
    release_year = db.Column(db.Integer)
    developer = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    rating = db.Column(db.Float)
    notes = db.Column(db.Text)

    def __repr__(self):
        """Returns a string representation of a game entry for debugging"""
        return f'<Game {self.title} ({self.platform})>'
