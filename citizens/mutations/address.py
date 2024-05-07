import graphene
from ..types.types import AddressType
from ..models import Address, Locality


class CreateAddress(graphene.Mutation):
    address = graphene.Field(AddressType)
    class Arguments:
        index = graphene.String(required=True)
        street = graphene.String()
        house = graphene.String(required=True)
        flat = graphene.String()
        locality = graphene.Int()
    def mutate(self, info, **kwargs):
        try:
            entry = Locality.objects.get(pk=kwargs["locality"])
        except Locality.DoesNotExist:
            entry = None

        new_address = Address(
            index=kwargs.get("index", None),
            street=kwargs.get("street", None),
            house=kwargs.get("house", None),
            flat=kwargs.get("flat", None),
            locality=entry
        )
        new_address.save()
        return CreateAddress(address=new_address)


class UpdateAddress(graphene.Mutation):
    ok = graphene.Boolean()
    address = graphene.Field(AddressType)

    class Arguments:
        address_id = graphene.ID(required=True)
        index = graphene.String()
        street = graphene.String()
        house = graphene.String()
        flat = graphene.String()
        locality = graphene.Int()

    def mutate(self, info, **kwargs):
        address = Address.objects.get(pk=kwargs["address_id"])
        try:
            entry = Locality.objects.get(pk=kwargs["locality"])
        except Locality.DoesNotExist:
            entry = None

        address.index=kwargs.get("index")
        address.street=kwargs.get("street")
        address.house=kwargs.get("house")
        address.flat=kwargs.get("flat")
        address.locality=entry

        address.save()

        return UpdateAddress(ok=True, address=address)

class DeleteAddress(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        address_id = graphene.ID(required=True)

    def mutate(self, info, address_id):
        address = Address.objects.get(pk=address_id)
        address.delete()
        return DeleteAddress(ok=True)