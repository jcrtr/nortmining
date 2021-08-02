import sqlalchemy as db
from backend.db import BaseModel


class Coin(BaseModel):
    __tablename__ = 'coin'

    name = db.Column(db.String(50))
    symbol = db.Column(db.String(50), unique=True)
    price_usd = db.Column(db.BigInteger)
    avr_usd = db.Column(db.BigInteger)


class Estimated(BaseModel):
    __tablename__ = 'estimated'

    eth = db.Column(db.Numeric(12, 6), default=0)


class WalletDeposit(BaseModel):
    __tablename__ = 'wallet_deposit'

    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=False)
    address = db.Column(db.String(100))
    insertTime = db.Column(db.BigInteger)
    is_binance = db.Column(db.Boolean, default=True)


class WalletWithdraw(BaseModel):
    __tablename__ = 'wallet_withdraw'

    id_b = db.Column(db.String(100), primary_key=True)
    amount = db.Column(db.String(50))
    coin = db.Column(db.String(50))
    address = db.Column(db.String(50))
    applyTime = db.Column(db.String(50))
    is_binance = db.Column(db.Boolean, default=True)
