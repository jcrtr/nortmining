from backend.utils.user.balance import update_balance
from backend.utils.user.sql.get import sql_get_user_id

from backend.utils.binance.sql.create import create_wallet_deposit_all, create_wallet_deposit, create_wallet_withdraw


async def handler(operate, data, db_data):
    """
    1 = Deposit
    2 = Withdraw
    """
    item_num = 0
    print(db_data)
    # print(data[0]['insertTime'])
    if operate == 1:
        if len(db_data) == 0:
            await create_wallet_deposit_all(data)
        else:
            while True:
                if len(db_data) == 0:
                    print('end')
                    break
                else:
                    item = data[item_num]['insertTime']
                    print(item)
                    print(item_num)
                    if item in db_data:
                        item_num += 1
                        print(f'Есть в базе: {item}')
                        db_data.remove(item)
                    else:
                        print('create')
                        await create_wallet_deposit(data[item_num])
                        await user_balance_update(operate, data[item_num])
                        item_num += 1
    else:
        pass
        # item = db_data[0]['id']
        # if item in db_data:
        #     db_data.remove(f'{item}')
        # else:
        # print('create')
        # amount = float(data['amount'])
        # time = int(data['applyTime'])
        # await create_wallet_withdraw(data[0])
        # await user_balance_update(operate, amount, time)


async def user_balance_update(operate, data):
    user_all = await sql_get_user_id()
    amount = float(data['amount'])
    time = int(data['insertTime'])

    while True:
        if len(user_all) == 0:
            break
        else:
            user_id = user_all[0]

            await update_balance(
                operate=operate,
                user_id=user_id,
                amount=amount,
                time=time
            )

            user_all.remove(f'{user_id}')
