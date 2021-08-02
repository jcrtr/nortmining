from backend.wallet.eth import WalletDeposit, WalletWithdraw


async def sql_get_wallet_deposit():
    result_db = await WalletDeposit.select('insertTime').gino.all()
    result = [wallet_deposit.insertTime for wallet_deposit in result_db]
    return result


async def sql_get_wallet_withdraw():
    result_db = await WalletWithdraw.select('id').gino.all()
    result = [wallet_withdraw.id for wallet_withdraw in result_db]
    return result
