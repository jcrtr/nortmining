from .base import BaseModel
from . import db


class Farm(BaseModel):
    __tablename__ = 'farm'

    name = db.Column(db.String(50), unique=True)
    reported = db.Column(db.Float)
    consumption = db.Column(db.Float)


class FarmUser(BaseModel):
    __tablename__ = 'capacity'

    user_id = db.Column(db.ForeignKey('user.id'))
    farm_id = db.Column(db.ForeignKey('farm.name'))
    name = db.Column(db.String(50))
    hash = db.Column(db.Float)
    consumption = db.Column(db.Float)
    percent = db.Column(db.Integer)
