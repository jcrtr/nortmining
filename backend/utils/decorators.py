from aiohttp import web
from graphql import GraphQLError


def login_required(func):
    async def wrapper(request):
        if not request.user:
            return web.json_response({'message': 'Auth required'}, status=401)
        return func(request)
    return wrapper


def login_required_graph(func):
    async def wrapper(root, info):
        if not info.context['is_authenticated']:
            return GraphQLError('Authorization error.')
        return func(root, info)
    return wrapper
