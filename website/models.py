from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    entry = db.relationship('Mood_Tracker')

class Mood_Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    trigger = db.Column(db.Text())
    preferred_approach = db.Column(db.Text())
    better_approach = db.Column(db.Text())
    Resolution = db.Column(db.Text())
    Satisfaction_rate = db.Column(db.Integer)