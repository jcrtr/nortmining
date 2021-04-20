import requests
from ...config import URL_POOL, WALLET
from ..user.sql.get import sql_get_user_id, sql_get_commission, sql_get_user_percent_hash
from .sql.create import sql_create_estimate
from .sql.update import sql_update_user_estimated


async def receive_estimate():
    payload = {}
    headers = {}

    url = URL_POOL + WALLET + "/currentStats"
    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()['data']
    reported = data['coinsPerMin']

    await sql_create_estimate(reported)
    await update_user_estimate(reported)


async def update_user_estimate(reported):
    users = await sql_get_user_id()

    while True:
        if len(users) == 0:
            break
        else:
            user_id = users[0]

            percent = await sql_get_commission(user_id)
            percent_hash = await sql_get_user_percent_hash(user_id)

            if percent == 0:
                estimated = (reported * percent_hash) * 60
            else:
                percent_reported = reported - (reported * percent)
                estimated = (percent_reported * percent_hash) * 60

            await sql_update_user_estimated(estimated, user_id)

            users.remove(f'{user_id}')
