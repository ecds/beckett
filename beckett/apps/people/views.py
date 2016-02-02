from django.shortcuts import render
from django.views.generic import ListView
from beckett.apps.people.models import Person

class PeopleList(ListView):
    model = Person