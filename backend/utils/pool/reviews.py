from .estimated import receive_estimate
from .farm import receive_farm


async def main_pool():
    await receive_farm()
    await receive_estimate()

