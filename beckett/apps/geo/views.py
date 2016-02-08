from django.shortcuts import render
from django.views.generic import ListView
from beckett.apps.geo.models import Repository

class RepositoryList(ListView):
    model = Repository