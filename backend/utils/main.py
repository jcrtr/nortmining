from backend.utils.binance.balance import receive_binance_balance
from .eth import receive_eth_price
from .farm import receive_farm

API_KEY = 'DjJL4NySy7o64uzhpRk1H4OAOobzY3n0keXevV9pGAmyQUeeaE35CIIReyvXJW5q'
API_SECRET = 'xrCv7faH8Xg3cvgCZwNbwbVHQogMhJVf51K7r3NKtd9wRGHHudWU7faraAv8NcRv'

eth_coin_url = "https://api.coincap.io/v2/assets/ethereum"
binance_balance_url = "https://api.binance.com/api/v3/account?"
pool_url = 'https://api.ethermine.org/miner/'
wallet = '0x460a6deec1d52c9c397e92fdc8c4bc05d10f8429'


async def main_utils():
    eth_price = await receive_eth_price(eth_coin_url)
    binance_balance = await receive_binance_balance(binance_balance_url, API_KEY, API_SECRET)
    farm = await receive_farm(pool_url, wallet)

