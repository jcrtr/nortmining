from backend.decorators import login_required
from backend.models.eth import Coin
from backend.utils.binance.main import main_binance


@login_required
async def coin_add(request):
    await Coin.create(
        name="ETH",
        symbol="ETH"
    )


async def deposit(request, **kwargs):
    await main_binance()
