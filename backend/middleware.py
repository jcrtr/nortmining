import json
import jwt
from aiohttp import web

from backend.config import JWT_SECRET, JWT_ALGORITHM
from backend.models.users import User


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token,
                                     JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return web.json_response({'message': 'Token is invalid'}, status=400)

            request.user = await User.get(payload['user_id'])
        return await handler(request)
    return middleware


async def auth_middleware_graph(app, handler):
    async def middleware(info):
        info.user = None
        jwt_token = info.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token,
                                     JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return web.json_response({'message': 'Token is invalid'}, status=400)

            info.user = await User.get(payload['user_id'])
        return await handler(info)
    return middleware
