from flask import Flask
from backend.models import db  # Make sure this points to the correct location

app = Flask(__name__)

# Configure SQLite database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
