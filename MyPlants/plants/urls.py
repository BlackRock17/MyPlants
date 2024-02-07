from django.urls import path

from MyPlants.plants import views

urlpatterns = (
    path("create/", views.create_plant, name="create-plant"),
    path("edit/<int:fruit_id>/", views.edit_plant, name="edit-plant"),
    path("details/<int:plant_id>/", views.details_plant, name="details-plant"),
    path("delete/<int:plant_id>/", views.delete_plant, name="delete-plant"),
)
