from .binance.reviews import main_binance
from .coin.reviews import main_coin
from .pool.reviews import main_pool
from .user.reviews import main_user


async def main_utils():
    await main_binance()
    await main_coin()
    await main_pool()
    await main_user()
