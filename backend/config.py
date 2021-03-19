from sqlalchemy.engine.url import URL

DB_DSN = URL(
    drivername='postgresql+asyncpg',
    username='db_user',
    password='Cnfhbr09',
    host='localhost',
    port=5432,
    database='miner_db',
)

JWT_SECRET = 'likiblack'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

WALLET = '0x460a6deec1d52c9c397e92fdc8c4bc05d10f8429'
API_KEY = 'DjJL4NySy7o64uzhpRk1H4OAOobzY3n0keXevV9pGAmyQUeeaE35CIIReyvXJW5q'
API_SECRET = 'xrCv7faH8Xg3cvgCZwNbwbVHQogMhJVf51K7r3NKtd9wRGHHudWU7faraAv8NcRv'
