from aiohttp import web
from aiohttp_session import new_session, get_session
from sqlalchemy.future import select

from backend.user.models import User
from backend.utils.views import main_utils
import aiohttp_sqlalchemy as ahsa


async def login(request):
    sa_session = ahsa.get_session(request)

    data = await request.json()
    device_id = request.headers.get('device_id')

    try:
        async with sa_session.begin():
            stmt = select(User).where(User.email == data['email']).first()
            user = await sa_session.execute(stmt)

        if not user.fetchone():
            return web.json_response({'message': 'Invalid email or password'}, status=400)

        if user.password != data['password']:
            return web.json_response({'message': 'Invalid email or password'}, status=400)

        session = await new_session(request)
        session['user'] = str(user.id)
        session['device'] = str(device_id)

        return web.Response(text='ok', status=200)

    except Exception:
        return web.json_response({'message': 'Error'}, status=400)


async def sing_out(request):
    session = await get_session(request)
    session.invalidate()
    print(f'logout:{session}')
    return web.Response(text='ok', status=200)


async def get_update(request):
    await main_utils()
    pass
