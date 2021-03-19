from urllib.parse import urlparse
from backend.models.eth import WalletDeposit
import hashlib
import hmac
import time
import urllib
import requests

from backend.models.users import UserDeposit, UserHash, User
from backend.utils.eth import receive_eth_price
from backend.utils.main import eth_coin_url


async def deposit(API_KEY, API_SECRET, **kwargs):
    API_SECRET = bytearray(API_SECRET, encoding='utf-8')

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

    response = requests.request("GET", url=url, data='', headers=headers)
    data = response.json()
    print(len(data))

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
                    await user_balance_deposit_update(data)
                    item_num += 1


async def user_balance_deposit_update(data):

    result_db_user = await User.select('id').gino.all()
    result_user_all = [user.id for user in result_db_user]

    while True:
        if len(result_user_all) == 0:
            break
        else:
            user_id = result_user_all[0]

            user_hash = await UserHash.select('percent_hash').where(UserHash.user_id == user_id).gino.all()
            user_percent_hash = [user.percent_hash for user in user_hash][0]
            percent_hash = (int(user_percent_hash) / 100)

            eth_price = await receive_eth_price(user_percent_hash)

            ETH = int(data['amount']) * percent_hash
            USD = eth_price * ETH

            try:
                await UserDeposit.create(
                    user_id=user_id,
                    usd=USD,
                    eth=ETH,
                    insertTime=data['insertTime']
                )
                result_user.remove(f'{user_id}')
            except Exception:
                result_user.remove(f'{user_id}')
