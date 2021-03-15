from aiohttp import web


def login_required(func):
    def wrapper(request):
        if not request.user:
            return web.json_response({'message': 'Auth required'}, status=401)
        return func(request)
    return wrapper
