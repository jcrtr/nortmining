from aiohttp import web
from aiohttp_session import get_session
import aiohttp_sqlalchemy as ahsa
from sqlalchemy.future import select

from .user.models import User


async def request_user_middleware(app, handler):
    async def middleware(request):
        sa_session = ahsa.get_session(request)
        request.session = await get_session(request)
        request.user = None
        user_id = request.session.get('user')
        if user_id is not None:
            async with sa_session.begin():
                stmt = select(User).where(User.id == user_id)
                user = await sa_session.execute(stmt)
            request.user = user.fetchone()
        return await handler(request)
    return middleware


def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            return web.json_response({'message': 'Auth required'}, status=401)
        return await func(self, *args, **kwargs)
    return wrapped
