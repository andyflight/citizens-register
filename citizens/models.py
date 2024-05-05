from django.db import models


class Address(models.Model):
    index = models.CharField(max_length=10)
    street = models.CharField(max_length=100, blank=True, null=True)
    house = models.CharField(max_length=10)
    flat = models.CharField(max_length=10, blank=True, null=True)
    locality = models.ForeignKey('Locality', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'address'


class Citizen(models.Model):

    class Marital(models.TextChoices):
        Married = 'married'
        Single = 'single'
        Divorced = 'divorced'
        Widowed = 'widowed'

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    ipn = models.CharField(unique=True, max_length=100)
    marital_status = models.CharField(max_length=20, choices=Marital.choices)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'citizen'


class District(models.Model):
    name = models.CharField(max_length=100)
    terr_unit = models.ForeignKey('TerritoryUnit', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'district'


class Hromada(models.Model):
    class LocalityType(models.TextChoices):
        Urban = 'urban'
        Settlement = 'settlement'
        Rural = 'rural'

    type = models.CharField(max_length=20, choices=LocalityType.choices, default=LocalityType.Urban)
    name = models.CharField(max_length=100)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'hromada'


class Locality(models.Model):

    class LocalityType(models.TextChoices):
        Urban = 'urban'
        Settlement = 'settlement'
        Rural = 'rural'

    type = models.CharField(max_length=20, choices=LocalityType.choices, default=LocalityType.Urban)
    name = models.CharField(max_length=100)
    terr_unit = models.ForeignKey('TerritoryUnit', on_delete=models.CASCADE, blank=True, null=True)
    hromada = models.ForeignKey('Hromada', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'locality'


class Passport(models.Model):

    class PassportType(models.TextChoices):
        Interal = 'internal'
        International = 'international'
    class SexType(models.TextChoices):
        Male = 'male'
        Female = 'female'

    type = models.CharField(max_length=20, choices=PassportType.choices, default=PassportType.Interal)
    sex = models.CharField(max_length=20, choices=SexType.choices)
    number = models.CharField(unique=True, max_length=50)
    series = models.CharField(max_length=50, blank=True, null=True)
    issuing_authority = models.CharField(max_length=100)
    birth_date = models.DateField()
    expiration_date = models.DateField()
    citizen = models.ForeignKey('Citizen', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'passport'


class Phone(models.Model):

    class PhoneType(models.TextChoices):
        Landline = 'landline'
        Mobile = 'mobile'

    type = models.CharField(max_length=20, choices=PhoneType.choices, default=PhoneType.Mobile)
    number = models.CharField(unique=True, max_length=20)
    citizen = models.ForeignKey('Citizen', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'phone'


class TerritoryUnit(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'territory_unit'

