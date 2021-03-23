from backend.utils.binance.connect import connect_binance
from .utils import handler
from backend.config import URL_DEPOSIT, URL_WITHDRAW
from backend.utils.binance.sql.get import sql_get_wallet_deposit, sql_get_wallet_withdraw


async def deposit():
    data = await connect_binance(URL_DEPOSIT)
    db_data = await sql_get_wallet_deposit()
    await handler(operate=1, data=data, db_data=db_data)


async def withdraw():
    data = await connect_binance(URL_WITHDRAW)
    db_data = await sql_get_wallet_withdraw()
    await handler(operate=2, data=data, db_data=db_data)
