from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.geo.models import Repository, Place

class RepositoryList(ListView):
    model = Repository

class RepositoryDetail(DetailView):
    model = Repository
    queryset = Repository.objects.all()
    template_name = 'geo/repository_detail.html'

class PlaceDetail(DetailView):
    model = Place
    queryset = Place.objects.all()
    template_name = 'place/place_detail.html'