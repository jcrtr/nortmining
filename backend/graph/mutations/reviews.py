import graphene

from .auth import CreateUser, LoginUser
from .farm import CreateFarm


class Mutation(graphene.ObjectType):
    login = LoginUser.Field()
    create_user = CreateUser.Field()
    create_farm = CreateFarm.Field()
