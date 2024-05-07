import graphene
from ..types.types import CitizenType
from ..models import Citizen, Address


class CreateCitizen(graphene.Mutation):
    citizen = graphene.Field(CitizenType)
    class Arguments:
        name = graphene.String()
        last_name = graphene.String()
        father_name = graphene.String()
        ipn = graphene.String()
        marital_status = graphene.String()
        address = graphene.Int()

    def mutate(self, info, **kwargs):
        try:
            entry = Address.objects.get(pk=kwargs["address"])
        except Address.DoesNotExist:
            entry = None

        citizen = Citizen(
            name=kwargs.get("name"),
            last_name=kwargs.get("last_name"),
            father_name=kwargs.get("father_name"),
            ipn=kwargs.get("ipn"),
            marital_status=kwargs.get("marital_status"),
            address=entry
        )
        citizen.save()
        return CreateCitizen(citizen=citizen)


class UpdateCitizen(graphene.Mutation):
    ok = graphene.Boolean()
    citizen = graphene.Field(CitizenType)


    class Arguments:
        citizen_id = graphene.ID(required=True)
        name = graphene.String()
        last_name = graphene.String()
        father_name = graphene.String()
        ipn = graphene.String()
        marital_status = graphene.String()
        address = graphene.Int()

    def mutate(self, info, **kwargs):
        citizen = Citizen.objects.get(pk=kwargs["citizen_id"])
        try:
            entry = Address.objects.get(pk=kwargs["address"])
        except Address.DoesNotExist:
            entry = None

        citizen.name = kwargs.get("name")
        citizen.last_name = kwargs.get("last_name")
        citizen.father_name = kwargs.get("father_name")
        citizen.ipn = kwargs.get("ipn")
        citizen.marital_status = kwargs.get("marital_status")
        citizen.address = entry

        citizen.save()
        return UpdateCitizen(ok=True, citizen=citizen)

class DeleteCitizen(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        citizen_id = graphene.ID(required=True)

    def mutate(self, info, citizen_id):
        citizen = Citizen.objects.get(pk=citizen_id)
        citizen.delete()
        return DeleteCitizen(ok=True)