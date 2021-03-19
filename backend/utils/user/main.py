import time
from datetime import datetime

from backend.models.users import UserBalance


async def sql_get_balance(user_id):
    result_db = await UserBalance \
        .select('total_eth') \
        .where(UserBalance.user_id == user_id) \
        .order_by(UserBalance.date_created.asc()) \
        .gino.all()

    total_eth = [balance.total_eth for balance in result_db][0]
    return total_eth


async def sql_update_balance(user_id, USD, ETH):
    await UserBalance.update \
        .values(total_usd=USD, total_eth=ETH, date_update=int(time.time())) \
        .where(UserBalance.user_id == user_id) \
        .gino.status()


async def update_balance(operate, user_id, eth, eth_price):
    balance = sql_get_balance(user_id)

    if operate == 1:
        ETH = await balance + eth
        USD = await eth_price * ETH
        await sql_update_balance(user_id, USD, ETH)

    else:
        ETH = await balance - eth
        USD = await eth_price * ETH

        await UserBalance.update \
            .values(total_usd=USD, total_eth=ETH, date_update=int(time.time())) \
            .where(UserBalance.user_id == user_id) \
            .gino.status()
