from ..coin.eth import receive_eth_price
from .sql.create import sql_create_user_deposit, sql_create_user_payment
from .sql.get import sql_get_balance, sql_get_user_percent_hash, sql_get_commission, sql_get_total_earned
from .sql.update import sql_update_balance, sql_update_total_earned


async def update_balance(operate, user_id, amount, time):

    balance = await sql_get_balance(user_id)
    total_earned = await sql_get_total_earned(user_id)
    percent = await sql_get_user_percent_hash(user_id)
    commission = await sql_get_commission(user_id)
    eth_price = await receive_eth_price()

    if operate == 1:
        if commission <= 0:
            eth_commission = amount * percent
            eth = balance + eth_commission
        else:
            eth_mining = amount * percent
            eth_commission = eth_mining - (eth_mining * commission)
            eth = balance + eth_commission

        usd_mining = float(eth_price) * eth_commission
        usd = int(float(eth_price) * eth)
        await sql_create_user_deposit(
            user_id=user_id,
            usd=usd_mining,
            eth=eth_commission,
            insert_time=time
        )
        total_usd = total_earned + usd

        await sql_update_total_earned(
            user_id=user_id,
            usd=total_usd,
        )

    else:
        eth = balance - amount
        usd = eth_price * eth
        await sql_create_user_payment(
            user_id=user_id,
            usd=usd,
            eth=eth,
            apply_time=time
        )

    await sql_update_balance(
        user_id=user_id,
        usd=usd,
        eth=eth
    )
