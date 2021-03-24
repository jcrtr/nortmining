from ....models.farm import Farm, FarmUser


async def sql_get_farm_name():
    result_db = await Farm.select('name').gino.all()
    result = [farm.name for farm in result_db]
    return result


async def sql_get_farm_total_hash():
    result_db = await Farm.select('reported').gino.all()
    result = [farm_hash.reported for farm_hash in result_db]
    farm_hash_total = sum(result)
    return farm_hash_total


async def sql_get_farm_user_farm_id(user_id):
    result_db = await FarmUser. \
        select('farm_id').where(FarmUser.user_id == user_id).gino.all()
    result = [result.farm_id for result in result_db]
    return result


async def sql_get_farm_user_percent(user_id, item_farm):
    result_db = await FarmUser. \
        select('percent'). \
        where(FarmUser.user_id == user_id, FarmUser.farm_id == item_farm) \
        .gino.all()
    result = [result.percent for result in result_db][0]
    return result
