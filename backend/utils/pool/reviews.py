from .farm import receive_farm


async def main_pool():
    await receive_farm()
