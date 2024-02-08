from django.urls import path

from MyPlants.plants import views
from MyPlants.plants.views import CreatePlant, DetailsPlant, EditPlant, DeletePlant

urlpatterns = (
    path("create/", CreatePlant.as_view(), name="create-plant"),
    path("edit/<int:pk>/", EditPlant.as_view(), name="edit-plant"),
    path("details/<int:pk>/", DetailsPlant.as_view(), name="details-plant"),
    path("delete/<int:pk>/", DeletePlant.as_view(), name="delete-plant"),
)
