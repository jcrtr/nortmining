import graphene

from .types import UserType
from ...models.users import User


class QueryUser(graphene.ObjectType):

    user = graphene.Field(UserType)

    @staticmethod
    async def resolve_me(root, info, user_id):
        user = await User.query.where(User.user_id == user_id).gino.all()
        return user
