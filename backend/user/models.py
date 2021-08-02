import sqlalchemy as db
from backend.db import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    is_admin = db.Column(db.Boolean, default=False)
    commission = db.Column(db.Integer, default=10)

    username = db.Column(db.String(50), unique=True, nullable=True)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    about = db.Column(db.Text, nullable=True, default="Mining is your best investment")

    investing = db.Column(db.BigInteger, default=0)
    total_earned = db.Column(db.BigInteger, default=0)
    estimated = db.Column(db.Numeric(12, 6), default=0)

    usd = db.Column(db.BigInteger, default=0)
    eth = db.Column(db.Numeric(12, 6), default=0)

    total_hash = db.Column(db.Numeric(12, 2), default=0)
    percent_hash = db.Column(db.BigInteger, default=0)


class UserWallet(BaseModel):
    __tablename__ = 'user_wallet'

    user_id = db.Column(db.ForeignKey('user.id'))
    coin_symbol = db.Column(db.ForeignKey('coin.symbol'))
    address = db.Column(db.String(100), unique=True)


class UserTransactions(BaseModel):
    __tablename__ = 'user_transactions'

    user_id = db.Column(db.ForeignKey('user.id'))
    usd = db.Column(db.BigInteger)
    eth = db.Column(db.Numeric(12, 6))
    time = db.Column(db.BigInteger)
    deposit = db.Column(db.Boolean, default=True)
    is_binance = db.Column(db.Boolean, default=True)


# class UserPayments(BaseModel):
#     __tablename__ = 'user_payments'
#
#     user_id = db.Column(db.ForeignKey('user.id'))
#     usd = db.Column(db.BigInteger)
#     eth = db.Column(db.Numeric(12, 6))
#     apply_time = db.Column(db.BigInteger)
#     is_binance = db.Column(db.Boolean, default=True)
#
#
# class UserDeposit(db.Model):
#     __tablename__ = 'user_deposit'
#
#     id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
#     user_id = db.Column(db.ForeignKey('user.id'))
#     usd = db.Column(db.BigInteger)
#     eth = db.Column(db.Numeric(12, 6))
#     insert_time = db.Column(db.BigInteger)
#     is_binance = db.Column(db.Boolean, default=True)

