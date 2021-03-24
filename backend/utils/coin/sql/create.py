from ....models.eth import Coin


async def sql_create_coin(name, symbol, price_usd, avr_usd):
    await Coin.create(
        name=name,
        symbol=symbol,
        price_usd=price_usd,
        avr_usd=avr_usd,
    )
