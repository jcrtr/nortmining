import asyncpg
import requests
from backend.models.eth import Coin
from backend.models.farm import Farm


async def receive_farm(url, wallet):
    payload = {}
    headers = {}

    result_db = await Farm.select('name').gino.all()
    result = [farm.name for farm in result_db]

    while True:
        if len(result) == 0:
            print('end')
            break
        else:
            item = result[0]

            url_farm = url + wallet + '/worker/' + item + "/currentStats"
            response = requests.request("GET", url_farm, headers=headers, data=payload)

            data = response.json()['data']
            reported = data['reportedHashrate']

            await sql_check(item, reported)
            result.remove(f'{item}')


async def sql_check(item, reported):
    try:
        await Farm.create(
            name=item,
            reported=reported,
        )
    except asyncpg.exceptions.UniqueViolationError:
        await Farm.update.values(
            name=item,
            reported=reported,
        ).where(Farm.name == item).gino.status()
