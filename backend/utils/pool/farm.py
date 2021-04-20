import asyncpg
import requests
from ...config import URL_POOL, WALLET
from ..user.sql.get import sql_get_user_id
from .sql.create import sql_create_farm
from .sql.get import sql_get_farm_name, sql_get_farm_user_farm_id, sql_get_farm_user_percent
from .sql.update import sql_update_farm, sql_update_user_farm


async def receive_farm():
    payload = {}
    headers = {}

    farm = await sql_get_farm_name()

    while True:
        if len(farm) == 0:
            break
        else:
            item_farm = farm[0]

            url = URL_POOL + WALLET + '/worker/' + item_farm + "/currentStats"
            response = requests.request("GET", url, headers=headers, data=payload)

            data = response.json()['data']
            reported = data['reportedHashrate']

            await sql_check(item_farm, reported)
            farm.remove(f'{item_farm}')


async def sql_check(item_farm, reported):
    try:
        await sql_create_farm(item_farm, reported)
    except asyncpg.exceptions.UniqueViolationError:
        await sql_update_farm(item_farm, reported)
        await update_user_hash(item_farm, reported)


async def update_user_hash(item_farm, reported):
    users = await sql_get_user_id()

    while True:
        if len(users) == 0:
            break
        else:
            user_id = users[0]
            farm_id = await sql_get_farm_user_farm_id(user_id)

            if item_farm in farm_id:
                percent = await sql_get_farm_user_percent(user_id, item_farm)

                if percent == 0:
                    pass
                else:
                    if percent == 100:
                        pass
                    else:
                        reported = reported * (percent / 100)

                    await sql_update_user_farm(reported, user_id, item_farm)

            users.remove(f'{user_id}')
