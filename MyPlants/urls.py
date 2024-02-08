
from django.contrib import admin
from django.urls import path, include

from MyPlants.plants import views
from MyPlants.plants.views import HomePage, Catalogue

urlpatterns = [
    path("admin/", admin.site.urls),
    path("plants/", include("MyPlants.plants.urls")),
    path("profile/", include("MyPlants.user_profile.urls")),
    path("", HomePage.as_view(), name="home-page"),
    path("catalogue/", Catalogue.as_view(), name="catalogue"),
]
