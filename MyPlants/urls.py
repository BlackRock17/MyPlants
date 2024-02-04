
from django.contrib import admin
from django.urls import path, include

from MyPlants.plants import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("plants/", include("MyPlants.plants.urls")),
    path("profile/", include("MyPlants.user_profile.urls")),
    path("", views.home_page, name="home-page"),
    path("catalogue/", views.catalogue, name="catalogue"),
]
