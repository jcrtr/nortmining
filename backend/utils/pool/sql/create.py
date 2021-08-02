from backend.wallet.eth import Estimated
from backend.farm.models import Farm


async def sql_create_farm(item, reported):
    await Farm.create(
        name=item,
        reported=reported,
    )


async def sql_create_estimate(reported):
    await Estimated.create(
        eth=reported,
    )
