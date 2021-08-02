import sqlalchemy as db
from aiohttp_sqlalchemy import sa_session

from backend.db import BaseModel


class Farm(BaseModel):
    __tablename__ = 'farm'

    name = db.Column(db.String(50), unique=True)
    reported = db.Column(db.Float, default=0)
    consumption = db.Column(db.Float, default=100)


class FarmUser(BaseModel):
    __tablename__ = 'user_farm'

    user_id = db.Column(db.ForeignKey('user.id'))
    farm_id = db.Column(db.ForeignKey('farm.name'))
    name = db.Column(db.String(50))
    hash = db.Column(db.Float)
    consumption = db.Column(db.Float)
    percent = db.Column(db.Integer)

