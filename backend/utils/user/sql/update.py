import time

from backend.models.users import UserBalance


async def sql_update_balance(user_id, usd, eth):
    await UserBalance.update \
        .values(total_usd=usd, total_eth=eth, date_update=int(time.time())) \
        .where(UserBalance.user_id == user_id) \
        .gino.status()
