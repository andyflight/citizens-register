import graphene
from ..types.types import DistrictType
from ..models import District, TerritoryUnit


class CreateDistrict(graphene.Mutation):
    district = graphene.Field(DistrictType)
    class Arguments:
        name = graphene.String()
        territory = graphene.Int()

    def mutate(self, info, **kwargs):
        try:
            entry = TerritoryUnit.objects.get(pk=kwargs["territory"])
        except TerritoryUnit.DoesNotExist:
            entry = None

        district = District(
            name=kwargs.get("name"),
            terr_unit=entry
        )
        district.save()
        return CreateDistrict(district=district)


class UpdateDistrict(graphene.Mutation):
    ok = graphene.Boolean()
    district = graphene.Field(DistrictType)



    class Arguments:
        district_id = graphene.ID(required=True)
        name = graphene.String()
        territory = graphene.Int()

    def mutate(self, info, **kwargs):
        district = District.objects.get(pk=kwargs["district_id"])
        try:
            entry = TerritoryUnit.objects.get(pk=kwargs["territory"])
        except TerritoryUnit.DoesNotExist:
            entry = None

        district.name = kwargs.get("name")
        district.terr_unit = entry

        district.save()
        return UpdateDistrict(ok=True, district=district)

class DeleteDistrict(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        district_id = graphene.ID(required=True)

    def mutate(self, info, district_id):
        district = District.objects.get(pk=district_id)
        district.delete()
        return DeleteDistrict(ok=True)