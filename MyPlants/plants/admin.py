from django.contrib import admin

from MyPlants.plants.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
