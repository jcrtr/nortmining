import graphene
import asyncio
from graphql.execution.executors.asyncio import AsyncioExecutor
from aiohttp_graphql import GraphQLView

from ..auth.middleware import SessionMiddleware
from .mutations.reviews import Mutation
from .query.farm import QueryUserFarm
from .query.user import QueryUser, QueryUserTransaction


class QueryUser(
    QueryUser,
    QueryUserTransaction,
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
    query=QueryUser,
    mutation=Mutations
)


gql_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    middleware=[
        SessionMiddleware(),
    ],
    graphiql=True,
    batch=True,
    enable_async=True,
)
