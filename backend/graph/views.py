import sys

import graphene
import asyncio

import jwt
from graphql import GraphQLError
from graphql.execution.executors.asyncio import AsyncioExecutor

from aiohttp_graphql import GraphQLView

from .mutations.reviews import Mutation
from .query.reviews import UserQuery
from ..auth.token import check_blacklist
from ..config import JWT_SECRET, JWT_ALGORITHM


class Query(
    UserQuery,
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


class AuthorizationMiddleware(object):
    async def resolve(self, next, root, info, **args):
        auth_header = info.context['request'].headers.get('Authorization')
        if auth_header:
            try:
                payload = jwt.decode(auth_header, JWT_SECRET, algorithms=JWT_ALGORITHM)
                is_blacklisted_token = await check_blacklist(auth_header)
                if is_blacklisted_token:
                    return GraphQLError('Token blacklisted. Please log in again.')
                else:
                    user_id = payload['sub']

            except jwt.ExpiredSignatureError as e:
                return GraphQLError('Signature expired. Please log in again.')
            except jwt.InvalidTokenError:
                return GraphQLError('Invalid token. Please log in again.')

        return next(root, info, **args)


gql_view = GraphQLView(
    schema=schema,
    executor=AsyncioExecutor(loop=asyncio.get_event_loop()),
    middleware=[AuthorizationMiddleware()],
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
