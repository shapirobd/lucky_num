from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    app.init_app(app)


class User(db.model):

    __tablename__ = 'users'

    name = db.Column(db.Text, nullable=False)

    email = db.Column(db.Text, nullable=False)

    year = db.Column(db.Integer, nullable=False)

    color = db.Column(db.Text, nullable=False)

    @validates('name')
