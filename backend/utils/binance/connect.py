import hashlib
import hmac
import time
import urllib
import requests
from urllib.parse import urlparse
from backend.config import API_KEY, API_SECRET


async def connect_binance(url, **kwargs):
    SECRET = bytearray(API_SECRET, encoding='utf-8')

    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    payload = kwargs

    payload.update({'timestamp': int(time.time() * 1000)})
    payload_str = urllib.parse.urlencode(payload).encode('utf-8')

    sign = hmac.new(
        key=SECRET,
        msg=payload_str,
        digestmod=hashlib.sha256
    ).hexdigest()

    payload_str = payload_str.decode("utf-8") + "&signature=" + str(sign)

    url = url + payload_str

    response = requests.request("GET", url=url, data='', headers=headers)
    data = response.json()
    return data
