import graphene


class UserBalanceType(graphene.ObjectType):

    total_hash = graphene.Int()
    total_eth = graphene.Float()
    date_updated = graphene.Int()


class UserHash(graphene.ObjectType):
    total_hash = graphene.Float()
    percent = graphene.Int()
    date_updated = graphene.Int()


class UserDeposit(graphene.ObjectType):
    usd = graphene.Int()
    eth = graphene.Float()
    apply_time = graphene.Int()
    is_binance = graphene.Boolean()


class UserPayments(graphene.ObjectType):
    usd = graphene.Int()
    eth = graphene.Float()
    insert_time = graphene.Int()
    is_binance = graphene.Boolean()


class FarmType(graphene.ObjectType):
    name = graphene.String()
    hash = graphene.String()
    consumption = graphene.String()
