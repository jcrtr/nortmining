from ....models.eth import Coin


async def sql_update_coin(symbol, price_usd, avr_usd):
    await Coin.update.values(
        price_usd=price_usd,
        avr_usd=avr_usd,
    ).where(Coin.symbol == symbol).gino.status()
