from django.urls import path

from MyPlants.user_profile import views
from MyPlants.user_profile.views import CreateProfile, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path("create/", CreateProfile.as_view(), name="create-profile"),
    path("details/<int:pk>/", ProfileDetailsView.as_view(), name="details-profile"),
    path("edit/<int:pk>/", ProfileEditView.as_view(), name="edit-profile"),
    path("delete/<int:pk>/", ProfileDeleteView.as_view(), name="delete-profile"),
)
