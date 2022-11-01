from django.contrib import admin
from fabrikanten.models import Fabrikanten

# Register your models here.

class FabrikantenAdmin(admin.ModelAdmin):
    model = Fabrikanten


admin.site.register(Fabrikanten, FabrikantenAdmin)