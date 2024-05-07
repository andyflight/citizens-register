import graphene
from ..types.types import LocalityType
from ..models import Hromada, TerritoryUnit, Locality


class CreateLocality(graphene.Mutation):
    locality = graphene.Field(LocalityType)
    class Arguments:
        type = graphene.String()
        name = graphene.String()
        terr_unit = graphene.Int()
        hromada = graphene.Int()

    def mutate(self, info, **kwargs):
        try:
            hromada = Hromada.objects.get(pk=kwargs["hromada"])
        except Hromada.DoesNotExist:
            hromada = None

        try:
            terr_unit = TerritoryUnit.objects.get(pk=kwargs["terr_unit"])
        except TerritoryUnit.DoesNotExist:
            terr_unit = None

        locality = Locality(
            name=kwargs.get("name"),
            type=kwargs.get("type"),
            terr_unit=terr_unit,
            hromada=hromada
        )
        locality.save()
        return CreateLocality(locality=locality)


class UpdateLocality(graphene.Mutation):
    ok = graphene.Boolean()
    hromada = graphene.Field(LocalityType)



    class Arguments:
        locality_id = graphene.ID(required=True)
        type = graphene.String()
        name = graphene.String()
        district = graphene.Int()

    def mutate(self, info, **kwargs):
        locality = Locality.objects.get(pk=kwargs["locality_id"])
        try:
            hromada = Hromada.objects.get(pk=kwargs["hromada"])
        except Hromada.DoesNotExist:
            hromada = None
        try:
            terr_unit = TerritoryUnit.objects.get(pk=kwargs["terr_unit"])
        except TerritoryUnit.DoesNotExist:
            terr_unit = None

        locality.name = kwargs.get("name")
        locality.type = kwargs.get("type")
        locality.terr_unit = terr_unit
        locality.hromada = hromada

        locality.save()
        return UpdateLocality(ok=True, locality=locality)

class DeleteLocality(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        locality_id = graphene.ID(required=True)

    def mutate(self, info, locality_id):
        locality = Locality.objects.get(pk=locality_id)
        locality.delete()
        return DeleteLocality(ok=True)