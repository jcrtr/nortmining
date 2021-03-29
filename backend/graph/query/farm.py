import sys
import graphene
import jwt
from graphql import ResolveInfo

from ...auth.token import decode_auth_token
from ...config import JWT_SECRET, JWT_ALGORITHM
from ...models.farm import FarmUser
from .types import FarmType


class QueryUserFarm(graphene.ObjectType):
    farms = graphene.List(FarmType)

    @staticmethod
    async def resolve_farms(root, info):
        user_id = await decode_auth_token(info)
        farms = await FarmUser.query.where(FarmUser.user_id == user_id).gino.all()
        return farms
