from aiohttp import web

from backend.middleware import auth_middleware, auth_middleware_graph
from backend.models import db

from routes import init_routes

import aiohttp_cors


async def init_app():
    app = web.Application(middlewares=[
        db,
        # auth_middleware,
        auth_middleware_graph,
    ])
    # db.init_app(app, dict(
    #     dsn=DB_DSN,))
    cors = aiohttp_cors.setup(app)
    init_routes(app, cors)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    app['db'] = await db.set_bind(
        "postgresql+asyncpg://db_user:Cnfhbr09@localhost/miner_db",
    )
    print('connect')
    await db.gino.create_all()


async def on_shutdown(app):
    await app['db'].pop_bind().close()
