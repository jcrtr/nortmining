from aiohttp import web

import asyncio
import aiohttp_cors
from aiohttp_session import setup
import aioredis
from aiohttp_session.redis_storage import RedisStorage

from backend.models.db import db
from backend.utils.views import main_utils
from routes import init_routes

loop = asyncio.get_event_loop()


async def make_redis_pool():
    redis_address = ('127.0.0.1', '6379')
    return await aioredis.create_redis_pool(redis_address, timeout=1)


async def init_app():
    redis_pool = await make_redis_pool()
    storage = RedisStorage(redis_pool, cookie_name="NORT_MINING")

    async def dispose_redis_pool(app):
        redis_pool.close()
        await redis_pool.wait_closed()

    app = web.Application(middlewares=[db])

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    init_routes(app, cors)
    setup(app, storage)
    db.init_app(app, dict(dsn="postgresql+asyncpg://db_user:Cnfhbr09@localhost/miner_db"))

    app.on_startup.append(on_start)
    # app.on_cleanup.append(on_shutdown)
    app.on_cleanup.append(dispose_redis_pool)

    return app


async def on_start(app):
    # await db.set_bind(
    #     "postgresql+asyncpg://db_user:Cnfhbr09@localhost/miner_db",
    # )
    print('create db')
    await db.gino.create_all()
    try:
        loop.create_task(main_utils())
    except asyncio.CancelledError:
        pass


async def on_shutdown(app):
    await db.pop_bind().close()
