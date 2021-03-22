from backend.models.users import UserDeposit, UserPayments


async def create_user_deposit(user_id, usd, eth, insert_time):
    await UserDeposit.create(
        user_id=user_id,
        usd=usd,
        eth=eth,
        insert_time=insert_time
    )


async def create_user_payment(user_id, usd, eth, apply_time):
    await UserPayments.create(
        user_id=user_id,
        usd=usd,
        eth=eth,
        apply_time=apply_time
    )
