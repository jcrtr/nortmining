import graphene


class LoginInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()


class SignUpInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()
