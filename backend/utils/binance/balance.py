import hashlib
import hmac
import time
import urllib
import asyncpg
import requests

from backend.wallet.eth import BalanceWallet
from urllib.parse import urlparse


async def receive_binance_balance(url, API_KEY, API_SECRET, **kwargs):

    API_SECRET = bytearray(API_SECRET, encoding='utf-8')
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    payload = kwargs

    payload.update({'timestamp': int(time.time()*1000)})
    payload_str = urllib.parse.urlencode(payload).encode('utf-8')

    sign = hmac.new(
        key=API_SECRET,
        msg=payload_str,
        digestmod=hashlib.sha256
    ).hexdigest()

    payload_str = payload_str.decode("utf-8") + "&signature=" + str(sign)

    url = url + payload_str
    response = requests.request("GET", url=url, data='', headers=headers)
    data = response.json()['balances'][2]

    try:
        await BalanceWallet.create(
            coin_symbol=data['asset'],
            balance=data['free']
        )
    except asyncpg.exceptions.UniqueViolationError:
        await BalanceWallet.update.values(
            coin_symbol=data['asset'],
            balance=data['free']
        ).where(BalanceWallet.coin_symbol == data['asset']).gino.status()

    return data['free']
