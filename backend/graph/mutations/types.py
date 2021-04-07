import graphene


class LoginInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()
    fp = graphene.String()


class SignUpInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()


class FarmInput(graphene.InputObjectType):
    name = graphene.String()
    consumption = graphene.Float()
