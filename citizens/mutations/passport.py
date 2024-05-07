import graphene
from ..types.types import PassportType
from ..models import Citizen, Passport


class CreatePassport(graphene.Mutation):
    passport = graphene.Field(PassportType)
    class Arguments:
        type = graphene.String()
        sex = graphene.String()
        number = graphene.String()
        series = graphene.String()
        issuing_authority = graphene.String()
        birth_date = graphene.Date()
        expiration_date = graphene.Date()
        citizen = graphene.Int()
    def mutate(self, info, **kwargs):
        try:
            entry = Citizen.objects.get(pk=kwargs["citizen"])
        except Citizen.DoesNotExist:
            entry = None

        new_passport = Passport(
            type=kwargs.get("type"),
            sex=kwargs.get("sex"),
            number=kwargs.get("number"),
            series=kwargs.get("series"),
            issuing_authority=kwargs.get("issuing_authority"),
            birth_date=kwargs.get("birth_date"),
            expiration_date=kwargs.get("expiration_date"),
            citizen=entry
        )
        new_passport.save()
        return CreatePassport(passport=new_passport)


class UpdatePassport(graphene.Mutation):
    ok = graphene.Boolean()
    passport = graphene.Field(PassportType)


    class Arguments:
        passport_id = graphene.ID(required=True)
        type = graphene.String()
        sex = graphene.String()
        number = graphene.String()
        series = graphene.String()
        issuing_authority = graphene.String()
        birth_date = graphene.Date()
        expiration_date = graphene.Date()
        citizen = graphene.Int()

    def mutate(self, info, **kwargs):
        passport = Passport.objects.get(pk=kwargs["passport_id"])
        try:
            entry = Citizen.objects.get(pk=kwargs["citizen"])
        except Citizen.DoesNotExist:
            entry = None

        passport.type = kwargs.get("type")
        passport.sex = kwargs.get("sex")
        passport.number = kwargs.get("number")
        passport.series = kwargs.get("series")
        passport.issuing_authority = kwargs.get("issuing_authority")
        passport.birth_date = kwargs.get("birth_date")
        passport.expiration_date = kwargs.get("expiration_date")
        passport.citizen = entry

        passport.save()
        return UpdatePassport(ok=True, passport=passport)

class DeletePassport(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        passport_id = graphene.ID(required=True)

    def mutate(self, info, passport_id):
        passport = Passport.objects.get(pk=passport_id)
        passport.delete()
        return DeletePassport(ok=True)