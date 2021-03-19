from datetime import datetime
from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
import time


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
    date_created = db.Column(db.BigInteger, default=int(time.time()))


class PriceElect(BaseModel):
    __tablename__ = 'price_elect'

    price = db.Column(db.BigInteger)
