import graphene
from ..types.types import PhoneType
from ..models import Citizen, Phone


class CreatePhone(graphene.Mutation):
    phone = graphene.Field(PhoneType)
    class Arguments:
        type = graphene.String()
        number = graphene.String()
        citizen = graphene.Int()
    def mutate(self, info, **kwargs):
        try:
            entry = Citizen.objects.get(pk=kwargs["citizen"])
        except Citizen.DoesNotExist:
            entry = None

        phone = Phone(
            type=kwargs.get("type"),
            number=kwargs.get("number"),
            citizen=entry
        )
        phone.save()
        return CreatePhone(phone=phone)


class UpdatePhone(graphene.Mutation):
    ok = graphene.Boolean()
    phone = graphene.Field(PhoneType)


    class Arguments:
        phone_id = graphene.ID(required=True)
        type = graphene.String()
        number = graphene.String()
        citizen = graphene.Int()

    def mutate(self, info, **kwargs):
        phone = Phone.objects.get(pk=kwargs["phone_id"])
        try:
            entry = Citizen.objects.get(pk=kwargs["citizen"])
        except Citizen.DoesNotExist:
            entry = None

        phone.type = kwargs.get("type")
        phone.number = kwargs.get("number")
        phone.citizen = entry

        phone.save()
        return UpdatePhone(ok=True, phone=phone)

class DeletePhone(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone_id = graphene.ID(required=True)

    def mutate(self, info, phone_id):
        phone = Phone.objects.get(pk=phone_id)
        phone.delete()
        return DeletePhone(ok=True)