from backend.models.eth import WalletDeposit, WalletWithdraw


async def create_wallet_deposit_all(data):
    await WalletDeposit.insert().gino.all(data)


async def create_wallet_deposit(data):
    await WalletDeposit.insert().gino.all(data)


async def create_wallet_withdraw_all(data):
    WalletWithdraw.insert().gino.all(data)


async def create_wallet_withdraw(data):
    await WalletWithdraw.insert().gino.all(data)
