from backend.models.users import UserBalance
from backend.utils.views import main_utils


async def coin_add(request):
    await UserBalance.create(
        user_id='3e5d8d13-30f3-4be7-ab9a-2d4350f72111',
        total_usd=123123,
        total_eth=0.222,
    )


async def deposit(request, **kwargs):
    await main_utils()
