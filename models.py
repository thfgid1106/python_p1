from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), nullable = False)
    user_id = db.Column(db.String(32), nullable = False)
    password = db.Column(db.String(64), nullable = False)
