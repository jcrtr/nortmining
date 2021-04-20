import graphene

from ...auth.decorators import login_required_graph
from ...models.users import User, UserTransactions
from ..query.types import UserType, UserTransactionType


class QueryUser(graphene.ObjectType):
    me = graphene.Field(UserType)

    @staticmethod
    @login_required_graph
    async def resolve_me(root, info):
        user_id = info.context['user']
        me = await User.query.where(User.id == user_id).gino.first()
        return me


class QueryUserTransaction(graphene.ObjectType):
    transaction = graphene.List(UserTransactionType)

    @staticmethod
    @login_required_graph
    async def resolve_me(root, info):
        user_id = info.context['user']
        transaction = await UserTransactions.query.where(User.id == user_id).gino.all()
        return transaction
