from django.db import models

# Create your models here.


class Fabrikanten(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "fabrikanten"
        verbose_name_plural = "Fabrikanten"
    def __str__(self):
        return self.name