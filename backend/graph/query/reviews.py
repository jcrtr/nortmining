from backend.graph.query.farm import QueryUserFarm
from backend.graph.query.user import QueryUser


class UserQuery(
    QueryUser,
    QueryUserFarm,
):
    pass