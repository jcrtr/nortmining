import graphene


class UserType(graphene.ObjectType):
    username = graphene.String()
    phone = graphene.Int()
    email = graphene.String()

    first_name = graphene.String()
    last_name = graphene.String()
    about = graphene.String()

    investing = graphene.Int()
    total_earned = graphene.Int()

    estimated = graphene.Int()

    usd = graphene.String()
    eth = graphene.Float()

    total_hash = graphene.Float()
    percent = graphene.Int()


class UserTransactionType(graphene.ObjectType):
    usd = graphene.Int()
    eth = graphene.Float()
    time = graphene.Int()
    deposit = graphene.Boolean()
    is_binance = graphene.Boolean()


class FarmType(graphene.ObjectType):
    name = graphene.String()
    hash = graphene.String()
    consumption = graphene.String()
