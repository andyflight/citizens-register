import graphene
from ..types.types import TerritoryUnitType
from ..models import TerritoryUnit


class CreateTerritory(graphene.Mutation):
    territory = graphene.Field(TerritoryUnitType)
    class Arguments:
        name = graphene.String(required=True)
    def mutate(self, info, **kwargs):


        new_territory = TerritoryUnit(
            name=kwargs.get("name")
        )
        new_territory.save()
        return CreateTerritory(territory=new_territory)


class UpdateTerritory(graphene.Mutation):
    ok = graphene.Boolean()
    territory = graphene.Field(TerritoryUnitType)


    class Arguments:
        territory_id = graphene.ID(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        territory = TerritoryUnit.objects.get(pk=kwargs["territory_id"])

        territory.name=kwargs.get("name")

        territory.save()
        return UpdateTerritory(ok=True, territory=territory)

class DeleteTerritory(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        territory_id = graphene.ID(required=True)

    def mutate(self, info, territory_id):
        territory = TerritoryUnit.objects.get(pk=territory_id)
        territory.delete()
        return DeleteTerritory(ok=True)