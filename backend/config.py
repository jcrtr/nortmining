from sqlalchemy.engine.url import URL

DB_DSN = URL(
    drivername='postgresql+asyncpg',
    username='user_db',
    password='password',
    host='localhost',
    port=5432,
    database='test_db',
)

JWT_SECRET = 'likiblack'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 3600


WALLET = '0x460a6deec1d52c9c397e92fdc8c4bc05d10f8429'

URL_DEPOSIT = 'https://api.binance.com/sapi/v1/capital/deposit/hisrec?'
URL_WITHDRAW = 'https://api.binance.com/sapi/v1/capital/withdraw/history?'
API_KEY = ''
API_SECRET = ''

URL_ETH_PRICE = 'https://api.coincap.io/v2/assets/ethereum'

URL_POOL = 'https://api.ethermine.org/miner/'
