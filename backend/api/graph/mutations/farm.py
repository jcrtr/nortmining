import graphene

from .types import FarmInput
from backend.farm.models import Farm


class CreateFarm(graphene.Mutation):
    class Arguments:
        input = FarmInput(required=True)

    message = graphene.String()

    @staticmethod
    async def mutate(root, info, input):
        farm = await Farm.query.where(Farm.name == input.name).gino.all()
        if not farm:
            try:
                await Farm.create(name=input.name, consumption=input.consumption)
                return CreateFarm(message='Farm add')

            except Exception:
                return CreateFarm(message='Some error occurred. Please try again.')

        else:
            return CreateFarm(message='Farm already exists.')