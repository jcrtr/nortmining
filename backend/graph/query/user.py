import graphene

from ...auth.decorators import login_required_graph
from ...models import db
from ...models.users import User, UserBalance, UserHash, UserDeposit, UserPayments
from ..query.types import \
    UserType, \
    UserBalanceType, \
    UserHashType, \
    UserDepositType, \
    UserPaymentsType


class QueryUser(graphene.ObjectType):
    me = graphene.Field(UserType)

    @staticmethod
    @login_required_graph
    async def resolve_me(root, info):
        user_id = info.context['user']
        async with db.acquire(reuse=False):
            me = await User.query.where(User.id == user_id).gino.first()
        return me


class QueryUserBalance(graphene.ObjectType):
    balance = graphene.Field(UserBalanceType)

    @staticmethod
    @login_required_graph
    async def resolve_balance(root, info):
        user_id = info.context['user']
        print(user_id)
        async with db.acquire(reuse=False):
            balance = await UserBalance.query.where(UserBalance.user_id == user_id).gino.first()
        return balance


class QueryUserHash(graphene.ObjectType):
    hashrate = graphene.Field(UserHashType)

    @staticmethod
    @login_required_graph
    async def resolve_hashrate(root, info):
        user_id = info.context['user']
        print(user_id)
        async with db.acquire(reuse=False):
            hashrate = await UserHash.query.where(UserHash.user_id == user_id).gino.first()
        return hashrate


class QueryUserDeposit(graphene.ObjectType):
    deposit = graphene.List(UserDepositType)

    @staticmethod
    @login_required_graph
    async def resolve_deposit(root, info):
        user_id = info.context['user']
        print(user_id)
        async with db.acquire(reuse=False):
            deposit = await UserDeposit.query.where(UserDeposit.user_id == user_id).gino.all()
        return deposit


class QueryUserPayments(graphene.ObjectType):
    payments = graphene.List(UserPaymentsType)

    @staticmethod
    @login_required_graph
    async def resolve_payments(root, info):
        user_id = info.context['user']
        print(user_id)
        async with db.acquire(reuse=False):
            payments = await UserPayments.query.where(UserPayments.user_id == user_id).gino.all()
        return payments
