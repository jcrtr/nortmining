from backend.decorators import login_required
from backend.models.eth import Coin, WalletDeposit
import hashlib
import hmac
import time
import urllib
import requests
from urllib.parse import urlparse


@login_required
async def coin_add(request):
    await Coin.create(
        name="ETH",
        symbol="ETH"
    )


async def deposit(request, **kwargs):

    API_KEY = 'DjJL4NySy7o64uzhpRk1H4OAOobzY3n0keXevV9pGAmyQUeeaE35CIIReyvXJW5q'
    API_SECRET = 'xrCv7faH8Xg3cvgCZwNbwbVHQogMhJVf51K7r3NKtd9wRGHHudWU7faraAv8NcRv'

    url = 'https://api.binance.com/sapi/v1/capital/deposit/hisrec?'

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

    result_db = await WalletDeposit.select('insertTime').gino.all()
    result = [wallet_deposit.insertTime for wallet_deposit in result_db]
    print(result)
    response = requests.request("GET", url=url, data='', headers=headers)
    data = response.json()
    print(data)
    item_num = 0

    if len(result) == 0:
        await WalletDeposit.insert().gino.all(data)
    else:
        while True:
            if len(result) == 0:
                print('end')
                break
            else:
                item = data[item_num]['insertTime']
                if item in result:
                    item_num += 1
                    result.remove(item)
                else:
                    print('create')
                    await WalletDeposit.insert().gino.all(data[item_num])
                    item_num += 1
