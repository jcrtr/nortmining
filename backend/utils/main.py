from backend.utils.binance.balance import receive_binance_balance
from .eth import receive_eth_price
from .farm import receive_farm
from ..config import WALLET, API_KEY, API_SECRET

eth_coin_url = "https://api.coincap.io/v2/assets/ethereum"
binance_balance_url = "https://api.binance.com/api/v3/account?"
pool_url = 'https://api.ethermine.org/miner/'


async def main_utils():
    eth_price = await receive_eth_price(eth_coin_url)
    binance_balance = await receive_binance_balance(binance_balance_url, API_KEY, API_SECRET)
    farm = await receive_farm(pool_url, WALLET)

