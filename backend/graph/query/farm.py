import graphene

from .types import FarmType
from ...auth.decorators import login_required_graph
from ...models.farm import FarmUser


class QueryUserFarm(graphene.ObjectType):
    farms = graphene.List(FarmType)

    @staticmethod
    @login_required_graph
    async def resolve_farms(root, info):
        user_id = info.context['user']
        farms = await FarmUser.query.where(FarmUser.user_id == user_id).gino.all()
        return farms
