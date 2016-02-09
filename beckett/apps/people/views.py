from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.people.models import Person

class PeopleList(ListView):
    model = Person
    template_name = 'people/person_list.html'

class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all()
    template_name = 'people/person_detail.html'

