import graphene
import asyncio

from aiohttp import web
from graphql.execution.executors.asyncio import AsyncioExecutor
from aiohttp_graphql import GraphQLView
from ..auth.middleware import AuthorizationMiddleware
from .mutations.reviews import Mutation
from .query.farm import QueryUserFarm
from .query.user import QueryUser, QueryUserBalance, QueryUserHash, QueryUserDeposit, QueryUserPayments


class Query(
    QueryUser,
    QueryUserBalance,
    QueryUserHash,
    QueryUserDeposit,
    QueryUserPayments,
    QueryUserFarm,
    graphene.ObjectType
):
    pass


class Mutations(
    Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutations
)


gql_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    middleware=[
        AuthorizationMiddleware(),
    ],
    graphiql=False,
    batch=True,
    enable_async=True,
)


gqil_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    graphiql=True,
    enable_async=True,
)
