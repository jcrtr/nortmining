import asyncpg
import requests

from backend.config import URL_ETH_PRICE
from backend.models.eth import Coin


async def receive_eth_price():

    payload = {}
    headers = {}

    response = requests.request("GET", URL_ETH_PRICE, headers=headers, data=payload)
    data = response.json()['data']

    try:
        await Coin.create(
            name=data['name'],
            symbol=data['symbol'],
            price_usd=float(data['priceUsd']),
            avr_usd=float(data['vwap24Hr']),
        )
    except asyncpg.exceptions.UniqueViolationError:
        await Coin.update.values(
            price_usd=float(data['priceUsd']),
            avr_usd=float(data['vwap24Hr']),
        ).where(Coin.symbol == data['symbol']).gino.status()

    return data['priceUsd']
