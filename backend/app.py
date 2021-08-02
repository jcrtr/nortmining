from aiohttp import web

import asyncio
from aiohttp_session import setup, session_middleware
import aioredis
from aiohttp_session.redis_storage import RedisStorage

from backend.config import DB_DSN
from backend.db import metadata
from backend.middleware import request_user_middleware
from backend.utils.views import main_utils
from routes import init_routes
import aiohttp_sqlalchemy as ahsa


async def make_redis_pool():
    return await aioredis.create_redis_pool(
        address="redis://127.0.0.1",
        # db=REDIS_DB,
        # password=REDIS_PASS,
        # maxsize=int(REDIS_POOL_SIZE) or 10,
        # timeout=int(REDIS_TIMEOUT) or 60,
        encoding='utf-8',
    )


async def init_app():
    middlewares = [request_user_middleware]
    app = web.Application(middlewares=middlewares)
    redis_pool = await make_redis_pool()
    storage = RedisStorage(redis_pool, cookie_name="SESSION")

    init_routes(app)
    setup(app, storage)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)

    return app


async def on_start(app):
    ahsa.setup(app, [
        ahsa.bind(f'{DB_DSN}'),
    ])
    await ahsa.init_db(app, metadata)


async def on_shutdown(app):
    redis_session = await make_redis_pool()
    redis_session.close()
    await redis_session.wait_closed()
