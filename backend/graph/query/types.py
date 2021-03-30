import graphene


class UserType(graphene.ObjectType):
    username = graphene.String()
    phone = graphene.Int()
    email = graphene.String()

    first_name = graphene.String()
    last_name = graphene.String()
    about = graphene.String()
    # balance = graphene.List(lambda: UserBalanceType, name='balance')


class UserBalanceType(graphene.ObjectType):
    total_usd = graphene.Int()
    total_eth = graphene.Float()
    date_updated = graphene.Int()


class UserHashType(graphene.ObjectType):
    total_hash = graphene.Float()
    percent = graphene.Int()
    date_updated = graphene.Int()


class UserDepositType(graphene.ObjectType):
    usd = graphene.Int()
    eth = graphene.Float()
    apply_time = graphene.Int()
    is_binance = graphene.Boolean()


class UserPaymentsType(graphene.ObjectType):
    usd = graphene.Int()
    eth = graphene.Float()
    insert_time = graphene.Int()
    is_binance = graphene.Boolean()


class FarmType(graphene.ObjectType):
    name = graphene.String()
    hash = graphene.String()
    consumption = graphene.String()
