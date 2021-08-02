import time

from backend.farm.models import FarmUser
from backend.user.models import User
from ..pool.sql.get import sql_get_farm_total_hash
from ..user.sql.get import sql_get_user_id


async def hash_rate():
    total_hash = await sql_get_farm_total_hash()
    users = await sql_get_user_id()

    while True:
        if len(users) == 0:
            break
        else:
            item = users[0]
            db = await FarmUser.select('hash').where(FarmUser.user_id == item).gino.all()
            result = [result.hash for result in db]
            total = sum(result)

            try:
                percent = (total / total_hash) * 100
                percent_format = int(percent)
                await User.update.values(
                    total_hash=total,
                    percent_hash=percent_format,
                    date_update=int(time.time()),
                ).where(User.id == item).gino.status()

            except ZeroDivisionError:
                pass

            users.remove(f'{item}')



