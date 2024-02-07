from django.shortcuts import render
from MyPlants.user_profile.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, "home-page.html", context)


def catalogue(request):
    pass


def create_plant(request):
    pass


def details_plant(request, plant_id):
    pass


def edit_plant(request, plant_id):
    pass


def delete_plant(request, plant_id):
    pass