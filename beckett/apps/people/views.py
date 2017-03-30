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


def arikha(request):
  return render(request, 'arikha.html')

def boyle(request):
  return render(request, 'boyle.html')

def bray(request):
  return render(request, 'bray.html')

def devine(request):
  return render(request, 'devine.html')

def harvey(request):
  return render(request, 'harvey.html')

def hutchinson(request):
  return render(request, 'hutchinson.html')

def lieberson(request):
  return render(request, 'lieberson.html')

def megged(request):
  return render(request, 'megged.html')

def myron(request):
  return render(request, 'myron.html')  

def rosset(request):
  return render(request, 'rosset.html')

def schneider(request):
  return render(request, 'schneider.html')

