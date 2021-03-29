from backend.decorators import login_required
from backend.models.eth import Coin
from backend.utils.views import main_utils


async def coin_add(request):
    print(request.headers)


async def deposit(request, **kwargs):
    await main_utils()
