import graphene

from backend.utils.decorators import login_required_graph
from backend.farm.models import FarmUser
from backend.user.models import User, UserTransactions, UserWallet
from ..query.types import UserType, UserTransactionType, UserWalletType, FarmType


class QueryUser(graphene.ObjectType):
    me = graphene.Field(UserType)

    @staticmethod
    @login_required_graph
    async def resolve_me(root, info):
        user_id = info.context['user']
        me = await User.query.where(User.id == user_id).gino.first()
        print(f'ME: {user_id}')
        return me


class QueryUserWallet(graphene.ObjectType):
    wallets = graphene.List(UserWalletType)

    @staticmethod
    @login_required_graph
    async def resolve_wallets(root, info):
        user_id = info.context['user']
        wallets = await UserWallet.query.where(UserWallet.user_id == user_id).gino.all()
        return wallets


class QueryUserTransaction(graphene.ObjectType):
    transactions = graphene.List(UserTransactionType)

    @staticmethod
    @login_required_graph
    async def resolve_transactions(root, info):
        user_id = info.context['user']
        transactions = await UserTransactions.query.where(UserTransactions.user_id == user_id).gino.all()
        return transactions


class QueryUserFarm(graphene.ObjectType):
    farms = graphene.List(FarmType)

    @staticmethod
    @login_required_graph
    async def resolve_farms(root, info):
        user_id = info.context['user']
        farms = await FarmUser.query.where(FarmUser.user_id == user_id).gino.all()
        return farms
