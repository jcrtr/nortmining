import graphene


class FarmType(graphene.ObjectType):
    name = graphene.String()
    reported = graphene.String()
    consumption = graphene.String()
