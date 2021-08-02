import time
import uuid
import sqlalchemy as db
from sqlalchemy.dialects.postgresql import UUID

from backend.db import BaseModel
from backend.user.models import User


class BlacklistToken(BaseModel):
    __tablename__ = 'auth_blacklist_tokens'

    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.BigInteger, default=int(time.time()))


class RefreshSession(BaseModel):
    __tablename__ = 'auth_refresh_session'

    user_id = db.Column(db.ForeignKey(User.id))
    fingerprint = db.Column(db.String(500), unique=True, nullable=False)
