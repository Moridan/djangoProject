from django.db import models

# Create your models here.


class Fabrikanten(models.Model):
    name = models.CharField(max_length=256)
