import json
import jwt
from aiohttp import web
from graphql import GraphQLError

from backend.auth.token import check_blacklist, decode_auth_token
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


class AuthorizationMiddleware(object):
    async def resolve(self, next, root, info, **args):
        # auth_header = info.context['request'].headers.get('accessToken')
        auth_header = info.context['request'].cookies.get('accessToken')
        print(auth_header)
        if auth_header is not None:
            try:
                payload = await decode_auth_token(auth_header)
                is_blacklisted_token = await check_blacklist(auth_header)
                if is_blacklisted_token:
                    pass
                    # return GraphQLError('Token blacklisted. Please log in again.')
                else:
                    info.context['user'] = payload['sub']
                    info.context['is_authenticated'] = True
            except jwt.ExpiredSignatureError as e:
                return GraphQLError('Signature expired. Please log in again.')
            except jwt.InvalidTokenError:
                return GraphQLError('Invalid token. Please log in again.')
        else:
            info.context['is_authenticated'] = False
        return next(root, info, **args)
