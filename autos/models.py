from django.db import models


# Create your models here.

class Auto(models.Model):
    BENZINE = "BENZINE"
    DIESEL = "DIESEL"
    FUEL = (
        (BENZINE, 'Benzine'),
        (DIESEL, 'Diesel')
    )
    name = models.CharField(max_length=256, unique=True)
    build = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=8, choices=FUEL, default=BENZINE)

    class Meta:
        db_table = "autos"


class Fabrikant(models.Model):
    name = models.CharField(max_length=256, unique=True)

