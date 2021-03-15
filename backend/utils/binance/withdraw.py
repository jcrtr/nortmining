import hashlib
import hmac
import time
import urllib
import requests
from urllib.parse import urlparse

from backend.models.eth import WalletWithdraw


async def withdraw(API_KEY, API_SECRET,**kwargs):

    API_SECRET = bytearray(API_SECRET, encoding='utf-8')

    url = 'https://api.binance.com/sapi/v1/capital/withdraw/history?'

    API_SECRET = bytearray(API_SECRET, encoding='utf-8')
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    payload = kwargs

    payload.update({'timestamp': int(time.time() * 1000)})
    payload_str = urllib.parse.urlencode(payload).encode('utf-8')

    sign = hmac.new(
        key=API_SECRET,
        msg=payload_str,
        digestmod=hashlib.sha256
    ).hexdigest()

    payload_str = payload_str.decode("utf-8") + "&signature=" + str(sign)

    url = url + payload_str

    result_db = await WalletWithdraw.select('id').gino.all()
    result = [wallet_withdraw.id for wallet_withdraw in result_db]

    response = requests.request("GET", url=url, data='', headers=headers)
    data = response.json()
    print(len(data))

    item_num = 0

    while True:
        if len(result) == 0:
            break
        else:
            item = data[item_num]['id']
            if item in result:
                item_num += 1
                result.remove(f'{item}')
            else:
                print('create')
                await WalletWithdraw.insert().gino.all(data[item_num])
                item_num += 1
