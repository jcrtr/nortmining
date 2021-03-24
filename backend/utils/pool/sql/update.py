from ....models.farm import Farm, FarmUser


async def sql_update_farm(item, reported):
    await Farm.update.values(
        name=item,
        reported=reported,
    ).where(Farm.name == item).gino.status()


async def sql_update_farm_user(reported, user_id, item_farm):
    await FarmUser.update.values(
        hash=reported,
    ).where(FarmUser.user_id == user_id, FarmUser.farm_id == item_farm) \
        .gino.status()
