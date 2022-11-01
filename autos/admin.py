from django.contrib import admin
from autos.models import Auto


# Register your models here.

class AutoAdmin(admin.ModelAdmin):
    model = Auto
    list_filter = ("fuel_type",)


admin.site.register(Auto, AutoAdmin)

