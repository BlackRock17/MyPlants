from django.urls import path

from MyPlants.plants import views
from MyPlants.plants.views import CreatePlantView, DetailsPlantView, EditPlantView, DeletePlantView

urlpatterns = (
    path("create/", CreatePlantView.as_view(), name="create-plant"),
    path("edit/<int:pk>/", EditPlantView.as_view(), name="edit-plant"),
    path("details/<int:pk>/", DetailsPlantView.as_view(), name="details-plant"),
    path("delete/<int:pk>/", DeletePlantView.as_view(), name="delete-plant"),
)
