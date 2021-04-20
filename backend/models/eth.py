import time
import uuid

from sqlalchemy.dialects.postgresql import UUID

from .base import BaseModel
from .db import db


class Coin(BaseModel):
    __tablename__ = 'coin'

    name = db.Column(db.String(50))
    symbol = db.Column(db.String(50), unique=True)
    price_usd = db.Column(db.BigInteger)
    avr_usd = db.Column(db.BigInteger)


class Estimated(db.Model):
    __tablename__ = 'estimated'

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
    eth = db.Column(db.Numeric(12, 6), default=0)
    date_created = db.Column(db.BigInteger, default=int(time.time()))


class WalletDeposit(db.Model):
    __tablename__ = 'wallet_deposit'

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=False)
    address = db.Column(db.String(100))
    insertTime = db.Column(db.BigInteger)
    date_created = db.Column(db.BigInteger, default=int(time.time()))
    is_binance = db.Column(db.Boolean, default=True)


class WalletWithdraw(db.Model):
    __tablename__ = 'wallet_withdraw'

    id = db.Column(db.String(100), primary_key=True)
    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    address = db.Column(db.String(50))
    applyTime = db.Column(db.String(50))
    date_created = db.Column(db.BigInteger, default=int(time.time()))
    is_binance = db.Column(db.Boolean, default=True)
