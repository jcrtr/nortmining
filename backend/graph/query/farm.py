import sys
import graphene

from backend.auth.token import decode_auth_token
from backend.graph.query.types import FarmType
from backend.models.users import User


class QueryFarm(graphene.ObjectType):
    # category = graphene.List(FarmType, id=graphene.Int())
    farms = graphene.List(FarmType)

    @staticmethod
    async def resolve_farms(root, info):
        auth_header = info.context.get('authorization')
        if auth_header:
            resp = decode_auth_token(auth_header)
            if not isinstance(resp, str):
                print('dgfsdfg')
                user = await User.query.where(User.id == resp).gino.first()
            else:
                sys.tracebacklimit = -1
                return Exception(resp)
        else:
            sys.tracebacklimit = -1
            return Exception('Auth required')
