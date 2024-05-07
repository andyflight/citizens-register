
import graphene
from graphene_django import DjangoObjectType
from .models import Address, Citizen, Hromada, District, Locality, Passport, Phone, TerritoryUnit

class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = ("id", "index", "street", "house", "flat", "locality", "citizen_set")

class CitizenType(DjangoObjectType):
    class Meta:
        model = Citizen
        fields = ("id", "name", "last_name", "father_name", "ipn", "martial_status", "address", "passport_set", "phone_set")

class DistrictType(DjangoObjectType):
    class Meta:
        model = District
        fields = ("id", "name", "terr_unit", "hromada_set")


class HromadaType(DjangoObjectType):
    class Meta:
        model = Hromada
        fields = ("id", "type", "name", "district", "locality_set")


class LocalityType(DjangoObjectType):
    class Meta:
        model = Locality
        fields = ("id", "type", "name", "terr_unit", "hromada", "address_set")


class PassportType(DjangoObjectType):
    class Meta:
        model = Passport
        fields = ("id", "type", "sex", "number", "series", "issuing_authority", "birth_date", "birth_date", "expiration_date", "citizen")

class PhoneType(DjangoObjectType):
    class Meta:
        model = Phone
        fields = ("id", "number", "type", "citizen")


class TerritoryUnitType(DjangoObjectType):
    class Meta:
        model = TerritoryUnit
        fields = ("id", "name")


class Query(graphene.ObjectType):
    addresses = graphene.List(AddressType)
    passports = graphene.List(PassportType)
    territories = graphene.List(TerritoryUnitType)
    phones = graphene.List(PhoneType)
    citizens = graphene.List(CitizenType)
    districts = graphene.List(DistrictType)
    hromadas = graphene.List(HromadaType)
    localities = graphene.List(LocalityType)

    def resolve_addresses(self, info, **kwargs):
        return Address.objects.all()

    def resolve_passports(self, info, **kwargs):
        return Passport.objects.all()

    def resolve_territories(self, info, **kwargs):
        return TerritoryUnit.objects.all()

    def resolve_phones(self, info, **kwargs):
        return Phone.objects.all()

    def resolve_citizens(self, info, **kwargs):
        return Citizen.objects.all()

    def resolve_districts(self, info, **kwargs):
        return District.objects.all()

    def resolve_hromadas(self, info, **kwargs):
        return Hromada.objects.all()

    def resolve_localities(self, info, **kwargs):
        return Locality.objects.all()

schema = graphene.Schema(query=Query)


