import graphene

from .auth import CreateUser, LoginUser


class Mutation(graphene.ObjectType):
    login = LoginUser.Field()
    create_user = CreateUser.Field()
