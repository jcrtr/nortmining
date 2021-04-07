import time
from sqlalchemy.dialects.postgresql import UUID

from . import db

from .base import BaseModel
import uuid


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)

    username = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=True)

    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    about = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.BigInteger, default=int(time.time()))
    commission = db.Column(db.Integer, default=10)
    # is_admin = db.Column(db.Boolean, default=False)


class Wallet(BaseModel):
    __tablename__ = 'user_wallet'

    user_id = db.Column(db.ForeignKey('user.id'), unique=True)
    coin_symbol = db.Column(db.ForeignKey('coin.symbol'))
    address = db.Column(db.String(100), unique=True)


class UserBalance(BaseModel):
    __tablename__ = 'user_balance'

    user_id = db.Column(db.ForeignKey('user.id'), unique=True)
    total_usd = db.Column(db.BigInteger)
    total_eth = db.Column(db.Numeric(12, 6))
    date_update = db.Column(db.BigInteger, default=int(time.time()))


class UserHash(BaseModel):
    __tablename__ = 'user_hash'

    user_id = db.Column(db.ForeignKey('user.id'), unique=True)
    total_hash = db.Column(db.Numeric(12, 2))
    percent_hash = db.Column(db.BigInteger)
    date_update = db.Column(db.BigInteger, default=int(time.time()))


class UserPayments(BaseModel):
    __tablename__ = 'user_payments'

    user_id = db.Column(db.ForeignKey('user.id'))
    usd = db.Column(db.BigInteger)
    eth = db.Column(db.Numeric(12, 6))
    apply_time = db.Column(db.BigInteger)
    is_binance = db.Column(db.Boolean, default=True)


class UserDeposit(db.Model):
    __tablename__ = 'user_deposit'

    user_id = db.Column(db.ForeignKey('user.id'))
    usd = db.Column(db.BigInteger)
    eth = db.Column(db.Numeric(12, 6))
    insert_time = db.Column(db.BigInteger)
    is_binance = db.Column(db.Boolean, default=True)

