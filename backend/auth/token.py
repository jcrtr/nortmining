import jwt
from datetime import datetime, timedelta
from ..config import JWT_EXP_DELTA_SECONDS, JWT_SECRET, JWT_ALGORITHM
from ..models.users import BlacklistToken


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
    try:
        payload = jwt.decode(auth_token, JWT_SECRET)
        is_blacklisted_token = await check_blacklist(auth_token)
        if is_blacklisted_token:
            return 'Token blacklisted. Please log in again.'
        else:
            return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


async def check_blacklist(auth_token):

    res = await BlacklistToken.query.where(BlacklistToken.token == auth_token).gino.first()
    if res:
        return True
    else:
        return False
