from graphene_django import DjangoObjectType

from ..models import Address, Citizen, Hromada, District, Locality, Passport, Phone, TerritoryUnit


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
        fields = ("id", "name", "district_set")
