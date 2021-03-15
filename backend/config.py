from sqlalchemy.engine.url import URL

JWT_SECRET = 'likiblack'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

DB_DSN = URL(
    drivername='postgresql+asyncpg',
    username='db_user',
    password='Cnfhbr09',
    host='localhost',
    port=5432,
    database='miner_db',
)
