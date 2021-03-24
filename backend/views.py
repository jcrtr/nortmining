from backend.decorators import login_required
from backend.models.eth import Coin
from backend.utils.views import main_utils


@login_required
async def coin_add(request):
    await Coin.create(
        name="ETH",
        symbol="ETH"
    )


async def deposit(request, **kwargs):
    await main_utils()
