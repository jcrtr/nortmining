from backend.models.users import UserBalance, User, UserHash, Wallet


async def sql_get_user_id():
    result_db = await User.select('id').gino.all()
    result = [user.id for user in result_db]
    return result


async def sql_get_commission(user_id):
    """Get SQL commission"""
    result_db = await User.select('commission').where(User.id == user_id).gino.all()
    commission = [user.commission for user in result_db][0]
    return int(commission) / 100


async def sql_get_user_percent_hash(user_id):
    """Get SQL UserHash"""
    result_db = await UserHash\
        .select('percent_hash')\
        .where(UserHash.user_id == user_id)\
        .gino.all()
    percent = [user.commission for user in result_db][0]
    return float(percent) / 100


async def sql_get_balance(user_id):
    """Get SQL UserBalance"""
    result_db = await UserBalance \
        .select('total_eth') \
        .where(UserBalance.user_id == user_id) \
        .order_by(UserBalance.date_created.asc()) \
        .gino.all()

    total_eth = [balance.total_eth for balance in result_db][0]
    return float(total_eth)


async def sql_get_wallet(user_id):
    get_eth_wallet = Wallet.select('address') \
        .where(Wallet.user_id == user_id).gino.first()
    result = [wallet.address for wallet in get_eth_wallet]
    return result
