from django.shortcuts import render
from django.urls import reverse_lazy

from MyPlants.mixins.mixins import ProfileContextMixin
from MyPlants.plants.models import Plant
from MyPlants.user_profile.models import Profile
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView


class HomePageView(ProfileContextMixin, TemplateView):
    template_name = 'home-page.html'


class CatalogueView(ProfileContextMixin, ListView):
    template_name = 'catalogue.html'
    model = Plant


class CreatePlantView(ProfileContextMixin, CreateView):
    template_name = 'plants/create-plant.html'
    model = Plant
    fields = '__all__'
    success_url = reverse_lazy('catalogue')


class DetailsPlantView(ProfileContextMixin, DetailView):
    template_name = 'plants/plant-details.html'
    model = Plant


class EditPlantView(ProfileContextMixin, UpdateView):
    template_name = 'plants/edit-plant.html'
    model = Plant
    success_url = reverse_lazy('catalogue')
    fields = '__all__'


class DeletePlantView(ProfileContextMixin, DeleteView):
    template_name = 'plants/delete-plant.html'
    model = Plant
    success_url = reverse_lazy('catalogue')

