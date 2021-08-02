import graphene
from graphql import GraphQLError

from backend.utils.decorators import login_required_graph
from backend.auth.models import BlacklistToken, RefreshSession
from backend.user.models import User
from backend.api.graph.mutations.types import SignUpInput, LoginInput
from backend.auth.token import encode_auth_token, decode_auth_token


class LoginUser(graphene.Mutation):
    class Arguments:
        input = LoginInput(required=True)

    access_token = graphene.String()

    @staticmethod
    async def mutate(root, info, input):
        try:
            user = await User.query.where(User.email == input.email).gino.first()
            fp = input.fp

            if not user:
                return GraphQLError(message='Invalid email or password')

            if user.password != input.password:
                return GraphQLError(message='Invalid email or password')

            refresh_token = await RefreshSession.create(
                user_id=user.id,
                fingerprint=fp
            )

            access_token = await encode_auth_token(
                user_id=user.id,
                refresh_token=str(refresh_token.id)
            )

            print(refresh_token)
            return LoginUser(
                access_token=access_token,
            )

        except Exception:
            return GraphQLError(message='Try again')


class LoginUserRefresh(graphene.Mutation):
    message = graphene.String()

    @staticmethod
    @login_required_graph
    async def mutate(root, info):
        user_id = info.context['user']
        device_id = info.context['device_id']
        # access_token = info.context['request'].cookies.get('accessToken')
        # fingerprint = info.context['request'].headers.get('personalization_id')
        # payload = await decode_auth_token(access_token)
        # refresh_token = payload['jti']
        # check_session = await RefreshSession.query.where(
        #     RefreshSession.id == refresh_token and
        #     RefreshSession.user_id == user_id and
        #     RefreshSession.fingerprint == fingerprint
        # ).gino.all()
        # if not check_session:
        #     return GraphQLError(message='Errors')

        try:
            # access_token = await encode_auth_token(user_id=user_id, refresh_token=refresh_token)
            user = await User.query.where(User.id == user_id).gino.first()

            if not user:
                return GraphQLError(message='Errors')

            return LoginUserRefresh(message='ok')

        except Exception:
            return GraphQLError(message='Errors')


class LogoutUser(graphene.Mutation):
    message = graphene.String()

    @staticmethod
    # @login_required_graph
    async def mutate(root, info):
        access_token = info.context['request'].cookies.get('accessToken')
        payload = await decode_auth_token(access_token)
        refresh_token = payload['jti']

        if access_token is not None:
            print(access_token)
            print(refresh_token)
            try:
                await BlacklistToken.create(token=access_token)
                await RefreshSession.delete.where(RefreshSession.id == refresh_token).gino.status()
                return LogoutUser(message='Successfully logged out.')
            except Exception:
                return GraphQLError(message='Some error occurred. Please try again.')


class RegisterUser(graphene.Mutation):
    class Arguments:
        input = SignUpInput(required=True)

    message = graphene.String()

    @staticmethod
    async def mutate(root, info, input):
        user = await User.query.where(User.email == input.email).gino.all()
        if not user:
            try:
                await User.create(email=input.email, password=input.password)
                return RegisterUser(message='Successfully registered.')
            except Exception:
                return GraphQLError(message='Some error occurred. Please try again.')
        else:
            return GraphQLError(message='User already exists. Please Log in.')


class CheckToken(graphene.Mutation):
    message = graphene.String()

    @staticmethod
    @login_required_graph
    async def mutate(root, info):
        return CheckToken(message='ok')
