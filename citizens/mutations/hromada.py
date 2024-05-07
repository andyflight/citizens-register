import graphene
from ..types.types import HromadaType
from ..models import District, Hromada


class CreateHromada(graphene.Mutation):
    hromada = graphene.Field(HromadaType)
    class Arguments:
        type = graphene.String()
        name = graphene.String()
        district = graphene.Int()

    def mutate(self, info, **kwargs):
        try:
            entry = District.objects.get(pk=kwargs["district"])
        except District.DoesNotExist:
            entry = None

        hromada = District(
            name=kwargs.get("name"),
            type=kwargs.get("type"),
            district=entry
        )
        hromada.save()
        return CreateHromada(hromada=hromada)


class UpdateHromada(graphene.Mutation):
    ok = graphene.Boolean()
    hromada = graphene.Field(HromadaType)



    class Arguments:
        hromada_id = graphene.ID(required=True)
        type = graphene.String()
        name = graphene.String()
        district = graphene.Int()

    def mutate(self, info, **kwargs):
        hromada = Hromada.objects.get(pk=kwargs["hromada_id"])
        try:
            entry = District.objects.get(pk=kwargs["district"])
        except District.DoesNotExist:
            entry = None

        hromada.name = kwargs.get("name")
        hromada.type = kwargs.get("type")
        hromada.district = entry

        hromada.save()
        return UpdateHromada(ok=True, hromada=hromada)

class DeleteHromada(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        hromada_id = graphene.ID(required=True)

    def mutate(self, info, hromada_id):
        hromada = Hromada.objects.get(pk=hromada_id)
        hromada.delete()
        return DeleteHromada(ok=True)