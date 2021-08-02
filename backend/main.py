import asyncio
import os
from aiohttp import web
from app import init_app

# try:
#     import uvloop
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def main():
    app = init_app()
    print(f"Запущен: {format(os.getpid())} мс")
    web.run_app(app)


if __name__ == '__main__':
    main()
