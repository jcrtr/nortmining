from aiohttp import web
from backend.models import db

from routes import init_routes
from aiohttp_session import setup, SimpleCookieStorage
import aiohttp_cors


async def init_app():
    app = web.Application(
        middlewares=[
            db,
        ])
    # db.init_app(app, dict(
    #     dsn=DB_DSN,))
    cors = aiohttp_cors.setup(app)
    init_routes(app, cors)
    setup(app, SimpleCookieStorage())
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    app['db'] = await db.set_bind(
        "postgresql+asyncpg://db_user:Cnfhbr09@localhost/miner_db",
    )
    print('connect db')
    await db.gino.create_all()


async def on_shutdown(app):
    await db.pop_bind().close()
