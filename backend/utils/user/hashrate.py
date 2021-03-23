import time

from backend.models.farm import FarmUser
from backend.models.users import UserHash
from backend.utils.pool.sql.get import sql_get_farm_total_hash
from backend.utils.user.sql.get import sql_get_user_id


async def hash_rate():
    total_hash = await sql_get_farm_total_hash()
    users = await sql_get_user_id()

    while True:
        if len(users) == 0:
            print('end')
            break
        else:
            item = users[0]
            db = await FarmUser.select('hash').where(FarmUser.user_id == item).gino.all()
            result = [result.hash for result in db]
            total = sum(result)

            percent = (total / total_hash) * 100
            percent_format = format(percent, '.3f')

            await UserHash.update.values(
                user_id=item,
                total_hash=total,
                percent_hash=percent_format,
                date_update=int(time.time()),
            ).where(UserHash.user_id == item).gino.status()

            result.remove(f'{item}')


