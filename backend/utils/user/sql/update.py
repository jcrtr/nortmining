import time

from backend.user.models import User


async def sql_update_balance(user_id, usd, eth):
    await User.update \
        .values(usd=usd, eth=eth, date_update=int(time.time())) \
        .where(User.id == user_id) \
        .gino.status()


async def sql_update_total_earned(user_id, usd):
    await User.update \
        .values(usd=usd) \
        .where(User.id == user_id) \
        .gino.status()
