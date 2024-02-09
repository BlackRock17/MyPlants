from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyPlants.plants.models import Plant
from MyPlants.user_profile.models import Profile


class CreateProfile(CreateView):
    template_name = 'profile/create-profile.html'
    model = Profile
    fields = ('username', 'first_name', 'last_name',)
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    template_name = 'profile/profile-details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_plants = Plant.objects.count()
        context['total_plants'] = total_plants
        return context


class ProfileEditView(UpdateView):
    template_name = 'profile/edit-profile.html'
    model = Profile
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details-profile', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    template_name = 'profile/delete-profile.html'
    model = Profile
    success_url = reverse_lazy('home-page')