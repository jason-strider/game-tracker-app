from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    genre = db.Column(db.String(50))

    playtime = db.Column(db.Integer, default=0)

    completion_status = db.Column(db.String(20), nullable=False)

    release_year = db.Column(db.Integer)

    developer = db.Column(db.String(100))

    publisher = db.Column(db.String(100))

    personal_rating = db.Column(db.Integer)

    notes = db.Column(db.String(100))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database created successfully!")

