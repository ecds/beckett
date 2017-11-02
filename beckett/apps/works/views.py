from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.works.models import Production, Publication, Writing, Directing, Translating, Reading

# Create your views here.
class ProductionDetail(DetailView):
    model = Production
    queryset = Production.objects.all()
    template_name = 'works/production_detail.html'


class PublicationDetail(DetailView):
    model = Publication
    queryset = Publication.objects.all()
    template_name = 'works/publication_detail.html'


class WritingDetail(DetailView):
    model = Writing
    queryset = Writing.objects.all()
    template_name = 'works/writing_detail.html'


class DirectingDetail(DetailView):
    model = Directing
    queryset = Directing.objects.all()
    template_name = 'works/directing_detail.html'


class TranslatingDetail(DetailView):
    model = Translating
    queryset = Translating.objects.all()
    template_name = 'works/translating_detail.html'


class ReadingDetail(DetailView):
    model = Reading
    queryset = Reading.objects.all()
    template_name = 'works/reading_detail.html'