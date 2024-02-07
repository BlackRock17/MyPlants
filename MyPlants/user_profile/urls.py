from django.urls import path

from MyPlants.user_profile import views
from MyPlants.user_profile.views import CreateProfile

urlpatterns = (
    path("create/", CreateProfile.as_view(), name="create-profile"),
    path("details/", views.details_profile, name="details-profile"),
    path("edit/", views.edit_profile, name="edit-profile"),
    path("delete/", views.delete_profile, name="delete-profile"),
)
