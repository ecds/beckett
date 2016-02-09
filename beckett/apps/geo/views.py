from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.geo.models import Repository

class RepositoryList(ListView):
    model = Repository

class RepositoryDetail(DetailView):
    model = Repository
    queryset = Repository.objects.all()
    template_name = 'geo/repository_detail.html'
