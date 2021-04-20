import asyncio

from .binance.reviews import main_binance
from .coin.reviews import main_coin
from .pool.reviews import main_pool
from .user.reviews import main_user


async def main_utils():
    while True:
        print('Start utils')
        await main_coin()
        await main_pool()
        await main_user()
        await main_binance()
        print('Stop utils')
        await asyncio.sleep(600.0)
