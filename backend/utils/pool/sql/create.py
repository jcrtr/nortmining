from ....models.eth import Estimated
from ....models.farm import Farm


async def sql_create_farm(item, reported):
    await Farm.create(
        name=item,
        reported=reported,
    )


async def sql_create_estimate(reported):
    await Estimated.create(
        eth=reported,
    )
