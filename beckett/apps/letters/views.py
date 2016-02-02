from django.shortcuts import render
from django.views.generic import ListView
from beckett.apps.letters.models import Letter

class LettersList(ListView):
    model = Letter