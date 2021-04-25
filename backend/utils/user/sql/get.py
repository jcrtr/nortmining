from ....models.users import User, UserWallet


async def sql_get_user_id():
    result_db = await User.select('id').gino.all()
    result = [str(user.id) for user in result_db]
    return result


async def sql_get_commission(user_id):
    """Get SQL commission"""
    result_db = await User.select('commission').where(User.id == user_id).gino.all()
    commission = [user.commission for user in result_db][0]
    return float(commission) / 100


async def sql_get_user_percent_hash(user_id):
    """Get SQL UserHash"""
    result_db = await User\
        .select('percent_hash')\
        .where(User.id == user_id)\
        .gino.all()
    percent = [user.percent_hash for user in result_db][0]
    return float(percent) / 100


async def sql_get_balance(user_id):
    """Get SQL UserBalance"""
    result_db = await User \
        .select('eth') \
        .where(User.id == user_id) \
        .gino.all()

    total_eth = [balance.eth for balance in result_db][0]
    return float(total_eth)


async def sql_get_total_earned(user_id):
    result_db = await User \
        .select('total_earned') \
        .where(User.id == user_id) \
        .gino.all()

    total_earned = [balance.total_earned for balance in result_db][0]
    return int(total_earned)


async def sql_get_wallet(user_id):
    result_db = await UserWallet.select('address') \
        .where(UserWallet.user_id == user_id).gino.all()
    result = [wallet.address for wallet in result_db]
    return result
