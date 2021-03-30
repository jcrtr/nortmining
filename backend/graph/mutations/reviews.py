import graphene

from .auth import CreateUser, LoginUser, LogoutUser
from .farm import CreateFarm


class Mutation(graphene.ObjectType):
    login = LoginUser.Field()
    logout = LogoutUser.Field()
    create_user = CreateUser.Field()
    create_farm = CreateFarm.Field()
