import time
from ..user.balance import update_balance
from ..user.sql.get import sql_get_user_id, sql_get_wallet

from .sql.create import sql_create_wallet_deposit_all, sql_create_wallet_deposit, sql_create_wallet_withdraw


async def handler(operate, data, db_data):
    """
    1 = Deposit
    2 = Withdraw
    """
    num = len(data)
    item_num = 0
    if len(db_data) == 0:
        if operate == 1:
            await sql_create_wallet_deposit_all(data)
        else:
            await sql_create_wallet_withdraw(data)
    else:
        while True:
            if item_num >= num:
                break
            else:
                if operate == 1:
                    item = data[item_num]['insertTime']
                    if item in db_data:
                        db_data.remove(item)
                        item_num += 1
                    else:
                        print(data[item_num])
                        await sql_create_wallet_deposit(data[item_num])
                        await user_balance_update(operate, data[item_num])
                        item_num += 1
                else:
                    item = data[item_num]['id']
                    if item in db_data:
                        db_data.remove(f'{item}')
                        item_num += 1
                    else:
                        print('create')
                        await sql_create_wallet_withdraw(data[item_num])
                        await user_balance_update(operate, data[item_num])
                        item_num += 1
            # item_num -= 1

    # else:
    #     item = data[item_num]['id']
    # if item in db_data:
    #     item_num -= 1
    #     if operate == 1:
    #
    #     else:
    #         print(f'Withdraw: {item}')
    #         db_data.remove(f'{item}')
    # else:
    #     print('esle')
    #     if operate == 1:
    #         print(f'Create Deposit: {item}')
    #         # await sql_create_wallet_deposit(data[item_num])
    #     else:
    #         print(f'Create Withdraw: {item}')
    #         await sql_create_wallet_withdraw(data[item_num])
    #
    #     await user_balance_update(operate, data[item_num])
    #     item_num -= 1


async def user_balance_update(operate, data):
    user_all = await sql_get_user_id()
    amount = float(data['amount'])

    while True:
        if len(user_all) == 0:
            break
        else:
            user_id = user_all[0]

            if operate == 1:
                create_time = int(time.time())
                print(time)
                await update_balance(
                    operate=operate,
                    user_id=user_id,
                    amount=amount,
                    time=create_time
                )
            else:
                address = str(data['address'])
                wallet = await sql_get_wallet(user_id)
                if address in wallet:
                    create_time = int(time.time())
                    print('ok')
                    await update_balance(
                        operate=operate,
                        user_id=user_id,
                        amount=amount,
                        time=create_time,
                    )

            user_all.remove(f'{user_id}')
