from ....models.farm import Farm, FarmUser
from ....models.users import User


async def sql_update_farm(item, reported):
    await Farm.update.values(
        name=item,
        reported=reported,
    ).where(Farm.name == item).gino.status()


async def sql_update_user_farm(reported, user_id, item_farm):
    await FarmUser.update.values(
        hash=reported,
    ).where(FarmUser.user_id == user_id and FarmUser.farm_id == item_farm) \
        .gino.status()


async def sql_update_user_estimated(estimated, user_id):
    await User.update.values(
        estimated=estimated,
    ).where(User.id == user_id).gino.status()
