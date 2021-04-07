import graphene

from .auth import RegisterUser, LoginUser, LogoutUser, LoginUserRefresh, CheckToken
from .farm import CreateFarm


class Mutation(graphene.ObjectType):
    login = LoginUser.Field()
    logout = LogoutUser.Field()
    register = RegisterUser.Field()

    check_token = CheckToken.Field()
    refresh_token = LoginUserRefresh.Field()
    create_farm = CreateFarm.Field()
