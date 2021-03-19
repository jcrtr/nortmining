import time
import uuid

from sqlalchemy.dialects.postgresql import UUID

from .base import BaseModel
from . import db


class BalanceWallet(BaseModel):
    __tablename__ = 'balance'

    coin_symbol = db.Column(db.ForeignKey('coin.symbol'))
    balance = db.Column(db.BigInteger)


class WalletDeposit(db.Model):
    __tablename__ = 'wallet_deposit'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=False)
    address = db.Column(db.String(100))
    insertTime = db.Column(db.BigInteger)
    date_created = db.Column(db.BigInteger, default=int(time.time()))


class WalletWithdraw(db.Model):
    __tablename__ = 'wallet_withdraw'

    id = db.Column(db.String(100), primary_key=True)
    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    address = db.Column(db.String(50))
    applyTime = db.Column(db.String(50))
    date_created = db.Column(db.BigInteger, default=int(time.time()))


class Coin(BaseModel):
    __tablename__ = 'coin'

    name = db.Column(db.String(50))
    symbol = db.Column(db.String(50), unique=True)
    price_usd = db.Column(db.BigInteger)
    avr_usd = db.Column(db.BigInteger)


