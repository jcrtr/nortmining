import asyncpg
import requests

from ...config import URL_ETH_PRICE
from .sql.create import sql_create_coin
from .sql.update import sql_update_coin


async def receive_eth_price():

    payload = {}
    headers = {}

    response = requests.request("GET", URL_ETH_PRICE, headers=headers, data=payload)
    data = response.json()['data']

    try:
        await sql_create_coin(
            name=data['name'],
            symbol=data['symbol'],
            price_usd=float(data['priceUsd']),
            avr_usd=float(data['vwap24Hr']),
        )
    except asyncpg.exceptions.UniqueViolationError:
        await sql_update_coin(
            symbol=data['symbol'],
            price_usd=float(data['priceUsd']),
            avr_usd=float(data['vwap24Hr']),
        )

    return data['priceUsd']
