from backend.utils.user.balance import update_balance
from backend.utils.user.sql.get import sql_get_user_id, sql_get_wallet

from backend.utils.binance.sql.create import sql_create_wallet_deposit_all, sql_create_wallet_deposit, sql_create_wallet_withdraw


async def handler(operate, data, db_data):
    """
    1 = Deposit
    2 = Withdraw
    """
    item_num = len(db_data) - 1
    # print(db_data)
    # print(data[0]['insertTime'])
    # print(len(db_data))
    if len(db_data) == 0:
        if operate == 1:
            await sql_create_wallet_deposit_all(data)
        else:
            await sql_create_wallet_withdraw(data)
    else:
        while True:
            if len(db_data) == 0:
                print('end')
                break
            else:
                # print(len(db_data))
                if operate == 1:
                    item = data[item_num]['insertTime']
                else:
                    item = data[item_num]['id']

                # print(f'NUMBER: {item}')
                # print(f'СЧЕТЧИК: {item_num}')
                if item in db_data:
                    item_num -= 1
                    print(f'Есть в базе: {item}')
                    if operate == 1:
                        db_data.remove(item)
                    else:
                        db_data.remove(f'{item}')
                else:
                    print('create')
                    if operate == 1:
                        await sql_create_wallet_deposit(data[item_num])
                    else:
                        await sql_create_wallet_withdraw(data[item_num])

                    await user_balance_update(operate, data[item_num])
                    item_num -= 1
                # print(db_data)


async def user_balance_update(operate, data):
    user_all = await sql_get_user_id()
    amount = float(data['amount'])

    while True:
        if len(user_all) == 0:
            break
        else:
            user_id = user_all[0]
            if operate == 1:
                time = int(data['insertTime'])
                await update_balance(
                    operate=operate,
                    user_id=user_id,
                    amount=amount,
                    time=time
                )
            else:
                address = str(data['address'])
                wallet = await sql_get_wallet(user_id)

                if address in wallet:
                    time = int(data['applyTime'])
                    await update_balance(
                        operate=operate,
                        user_id=user_id,
                        amount=amount,
                        time=time,
                    )

            user_all.remove(f'{user_id}')
