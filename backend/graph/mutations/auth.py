import graphene
from backend.models.users import User, BlacklistToken
from backend.graph.mutations.types import SignUpInput, LoginInput
from backend.auth.token import encode_auth_token, decode_auth_token


class LoginUser(graphene.Mutation):
    class Arguments:
        input = LoginInput(required=True)

    message = graphene.String()
    token = graphene.String()

    @staticmethod
    async def mutate(root, info, input):
        try:
            user = await User.query.where(User.email == input.email).gino.first()
            print(user)
            if not user:
                return LoginUser(message='Invalid email or password')

            if user.password != input.password:
                return LoginUser(message='Invalid email or password')

            auth_token = await encode_auth_token(user_id=user.id)
            print(auth_token)
            # jwt_token = auth_token.decode()
            return LoginUser(
                message='Successfully logged in.',
                token=auth_token
            )
        except Exception:
            return LoginUser(message='Try again')


class LogoutUser(graphene.Mutation):
    message = graphene.String()
    token = graphene.String()

    @staticmethod
    async def mutate(root, info):
        auth_header = info.context.get('authorization')
        if auth_header:
            resp = decode_auth_token(auth_header)
            if not isinstance(resp, str):
                try:
                    await BlacklistToken.create(token=auth_header)
                    return LogoutUser(message='Successfully logged out.')
                except Exception as e:
                    return LogoutUser(message=e)
            else:
                return LogoutUser(
                    message=resp,
                )
        else:
            return LogoutUser(
                message='Provide a valid auth token.',
            )


class CreateUser(graphene.Mutation):
    class Arguments:
        input = SignUpInput(required=True)

    message = graphene.String()
    token = graphene.String()

    @staticmethod
    async def mutate(root, info, input):
        user = await User.query.where(User.email == input.email).gino.all()
        if not user:
            try:
                await User.create(email=input.email, password=input.password)
                return CreateUser(message='Successfully registered.')

            except Exception:
                return CreateUser(message='Some error occurred. Please try again.')

        else:
            return CreateUser(message='User already exists. Please Log in.')
