from datetime import datetime

from backend.models.eth import BalanceWallet
from backend.models.farm import Farm, Capacity
from backend.models.users import User, UserBalance, UserHash


async def coin(eth_price):
    # Баланс общий
    balance = await BalanceWallet.select('balance').where(BalanceWallet.coin_symbol == 'ETH').gino.all()
    balance_res = [balance.balance for balance in balance][0]
    print(balance_res)

    # Сумма хешрейта
    farm_hash = await Farm.select('reported').gino.all()
    farm_hash_res = [farm_hash.reported for farm_hash in farm_hash]
    farm_hash_total = sum(farm_hash_res)
    print(sum(farm_hash_res))

    # хешрейт пользваотелей
    user_db = await User.select('uuid_id').gino.all()
    user_db_result = [user_db.uuid_id for user_db in user_db]
    await farm_hash_user(user_db_result, farm_hash_total)


async def farm_hash_user(result, hash_all):
    while True:
        if len(result) == 0:
            print('end')
            break
        else:
            item = result[0]
            db = await Capacity.select('reported').where(Capacity.user_uuid == item).gino.all()
            result = [result.reported for result in db]
            total = sum(result)

            percent = (total / hash_all) * 100
            percent_format = format(percent, '.3f')

            await UserBalance.update.values(
                user_id=total,
                total_usd=percent_format,
                total_eth=datetime.utcnow,
            ).where(UserHash.user_id == item).gino.status()

            await UserHash.update.values(
                user_id=item,
                total_hash=total,
                percent_hash=percent_format,
                date_update=datetime.utcnow,
            ).where(UserHash.user_id == item).gino.status()

            result.remove(f'{item}')
