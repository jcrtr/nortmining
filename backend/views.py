from aiohttp import web
from aiohttp_session import new_session, get_session
from backend.models.users import User


async def login(request):
    data = await request.json()
    device_id = request.headers.get('device_id')

    try:
        user = await User.query.where(User.email == data['email']).gino.first()

        if not user:
            return web.json_response({'message': 'Invalid email or password'}, status=400)

        if user.password != data['password']:
            return web.json_response({'message': 'Invalid email or password'}, status=400)

        session = await new_session(request)
        session['user_id'] = str(user.id)
        session['device_id'] = str(device_id)

        print(f'new session: {session}')
        return web.Response(text='ok', status=200)

    except Exception:
        return web.json_response({'message': 'Invalid email or password'}, status=400)

async def sing_out(request):
    session = await get_session(request)
    session.invalidate()
    print(f'logout:{session}')
    return web.Response(text='ok', status=200)
