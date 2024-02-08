from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from MyPlants.user_profile.models import Profile


class CreateProfile(CreateView):
    template_name = 'profile/create-profile.html'
    model = Profile
    fields = ('username', 'first_name', 'last_name',)
    success_url = reverse_lazy('catalogue')


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
