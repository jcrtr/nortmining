from functools import wraps
import graphene

from backend.auth.token import decode_auth_token


class MessageField(graphene.ObjectType):
    message = graphene.String()


def mutation_header_jwt_required(fn):
    """
    A decorator to protect a mutation.
    If you decorate a mutation with this, it will ensure that the requester
    has a valid access token before allowing the mutation to be called. This
    does not check the freshness of the access token.
    """

    @wraps(fn)
    def wrapper(self, info):
        token = info.context['request'].headers.get('Authorization')
        try:
            user_id = decode_auth_token(token)
        except Exception as e:
            return MessageField(message=str(e))

        return fn(user_id)

    return wrapper
