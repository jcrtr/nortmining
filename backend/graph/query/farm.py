import sys
import graphene

from ...auth.token import decode_auth_token
from ...models.farm import FarmUser
from .types import FarmType


class QueryUserFarm(graphene.ObjectType):
    farms = graphene.List(FarmType)

    @staticmethod
    async def resolve_farms(root, info):
        auth_header = info.context.get('authorization')
        if auth_header:
            user_id = decode_auth_token(auth_header)
            if not isinstance(user_id, str):
                # user = await User.query.where(User.id == user_id).gino.first()
                farms = await FarmUser.query.where(FarmUser.user_id == user_id).gino.all()
                return farms
            else:
                sys.tracebacklimit = -1
                return Exception('Auth required')
        else:
            sys.tracebacklimit = -1
            return Exception('Auth required')


# class QueryFarm(graphene.ObjectType):
#     # category = graphene.List(FarmType, id=graphene.Int())
#     farms = graphene.List(FarmType)
#
#     @staticmethod
#     async def resolve_farms(root, info):
#         auth_header = info.context.get('authorization')
#         if auth_header:
#             resp = decode_auth_token(auth_header)
#             if not isinstance(resp, str):
#                 print('dgfsdfg')
#                 user = await User.query.where(User.id == resp).gino.first()
#             else:
#                 sys.tracebacklimit = -1
#                 return Exception(resp)
#         else:
#             sys.tracebacklimit = -1
#             return Exception('Auth required')
