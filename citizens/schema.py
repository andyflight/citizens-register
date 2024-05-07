
import graphene
from .models import Address, Citizen, Hromada, District, Locality, Passport, Phone, TerritoryUnit
from .types.types import AddressType, CitizenType, HromadaType, DistrictType, LocalityType, PassportType, PhoneType, TerritoryUnitType
from .mutations.address import CreateAddress, UpdateAddress, DeleteAddress
from .mutations.passport import CreatePassport, UpdatePassport, DeletePassport
from .mutations.territory import CreateTerritory, UpdateTerritory, DeleteTerritory
from .mutations.phone import CreatePhone, UpdatePhone, DeletePhone
from .mutations.citizen import CreateCitizen, UpdateCitizen, DeleteCitizen
from .mutations.district import CreateDistrict, UpdateDistrict, DeleteDistrict
from .mutations.hromada import CreateHromada, UpdateHromada, DeleteHromada
from .mutations.locality import CreateLocality, UpdateLocality, DeleteLocality

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


class Mutation(graphene.ObjectType):
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
    delete_address = DeleteAddress.Field()

    create_passport = CreatePassport.Field()
    update_passport = UpdatePassport.Field()
    delete_passport = DeletePassport.Field()

    create_territory = CreateTerritory.Field()
    update_territory = UpdateTerritory.Field()
    delete_territory = DeleteTerritory.Field()

    create_phone = CreatePhone.Field()
    update_phone = UpdatePhone.Field()
    delete_phone = DeletePhone.Field()

    create_citizen = CreateCitizen.Field()
    update_citizen = UpdateCitizen.Field()
    delete_citizen = DeleteCitizen.Field()

    create_district = CreateDistrict.Field()
    update_district = UpdateDistrict.Field()
    delete_district = DeleteDistrict.Field()

    create_hromada = CreateHromada.Field()
    update_hromada = UpdateHromada.Field()
    delete_hromada = DeleteHromada.Field()

    create_locality = CreateLocality.Field()
    update_locality = UpdateLocality.Field()
    delete_locality = DeleteLocality.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


