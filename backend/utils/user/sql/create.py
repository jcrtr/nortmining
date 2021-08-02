from backend.user.models import UserTransactions


async def sql_create_user_deposit(user_id, usd, eth, insert_time):
    await UserTransactions.create(
        user_id=user_id,
        usd=usd,
        eth=eth,
        deposit=True,
        time=insert_time
    )


async def sql_create_user_payment(user_id, usd, eth, apply_time):
    await UserTransactions.create(
        user_id=user_id,
        usd=usd,
        eth=eth,
        deposit=False,
        time=apply_time
    )
