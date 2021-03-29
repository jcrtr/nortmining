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


async def decode_auth_token(info):
    auth_token = info.context['request'].headers.get('Authorization')
    payload = jwt.decode(auth_token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    return payload['sub']


async def check_blacklist(auth_token):

    res = await BlacklistToken.query.where(BlacklistToken.token == auth_token).gino.first()
    if res:
        return True
    else:
        return False
