from django.db import models

from fabrikanten.models import Fabrikanten


# Create your models here.

class Auto(models.Model):
    BENZINE = "BENZINE"
    DIESEL = "DIESEL"
    FUEL = (
        (BENZINE, 'Benzine'),
        (DIESEL, 'Diesel')
    )
    name = models.CharField(max_length=256, unique=True)
    build = models.PositiveIntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=8, choices=FUEL, default=BENZINE)
    fabrikanten = models.ForeignKey(Fabrikanten, on_delete=models.CASCADE)

    class Meta:
        db_table = "autos"
