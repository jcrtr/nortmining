from ....models.farm import Farm


async def sql_create_farm(item, reported):
    await Farm.create(
        name=item,
        reported=reported,
    )
