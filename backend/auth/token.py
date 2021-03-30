import jwt
from datetime import datetime, timedelta
from graphql import GraphQLError

from ..config import JWT_EXP_DELTA_SECONDS, JWT_SECRET, JWT_ALGORITHM
from ..models import db
from ..models.users import BlacklistToken, User


async def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            'iat': datetime.utcnow(),
            'sub': str(user_id)
        }
        return jwt.encode(
            payload,
            JWT_SECRET,
            JWT_ALGORITHM,
        )
    except Exception as e:
        return e


async def decode_auth_token(auth_token):
    payload = jwt.decode(auth_token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload['sub']
    async with db.acquire(reuse=False):
        res = await User.select('id').where(User.id == user_id).gino.first()
        if res:
            return payload['sub']
        else:
            await BlacklistToken.create(token=auth_token)
            return GraphQLError('Error Token. Token add blacklisted.')


async def check_blacklist(auth_token):
    async with db.acquire(reuse=False):
        res = await BlacklistToken.query.where(BlacklistToken.token == auth_token).gino.first()
    return res

