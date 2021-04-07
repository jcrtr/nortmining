import time
import uuid
from sqlalchemy.dialects.postgresql import UUID
from . import db
from .users import User


class BlacklistToken(db.Model):

    __tablename__ = 'auth_blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.BigInteger, default=int(time.time()))


class RefreshSession(db.Model):
    __tablename__ = 'auth_refresh_session'

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.ForeignKey(User.id))
    fingerprint = db.Column(db.String(500), unique=True, nullable=False)
    create_date = db.Column(db.BigInteger, default=int(time.time()))
