import graphene

from .types import UserBalanceType
from ...auth.token import decode_auth_token
from ...models.users import UserBalance


class QueryUserFarm(graphene.ObjectType):
    user_balance = graphene.List(UserBalanceType)

    @staticmethod
    async def resolve_farms(root, info):
        auth_header = info.context.get('authorization')
        if auth_header:
            user_id = decode_auth_token(auth_header)
            if not isinstance(user_id, str):
                user_balance = await UserBalance\
                    .query.where(UserBalance.user_id == user_id)\
                    .gino.all()
                return user_balance
            else:
                sys.tracebacklimit = -1
                return Exception('Auth required')
        else:
            sys.tracebacklimit = -1
            return Exception('Auth required')
