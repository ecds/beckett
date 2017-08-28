from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.letters.models import Letter
from django.template import RequestContext
from beckett.apps.letters.forms import LetterSearchForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from collections import Counter


class LettersList(ListView):
    model = Letter

class LettersDetail(DetailView):
    model = Letter
    queryset = Letter.objects.all()
    template_name = 'letters/letter_detail.html'

def about(request):
  return render(request, 'about.html')

def searches(request):
    return render_to_response('searches.html')

def search_result(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        words = Letter.objects.filter(key_terms__icontains=q)
        return render_to_response('search_result.html',
            {'words': words, 'query': q})
    else:
        return HttpResponse('None Found.')

def get_recipients(request):
    q = request.GET.get('term', '')
    letters = Letter.objects.filter(recipients_excel__icontains = q)
    results = []
    for letter in letters:
        results.append(letter.recipients_excel)
    categorized_letters = Counter(results)

    unique_results = []
    for letter in letters:
        if letter.recipients_excel not in unique_results:
            unique_results.append(letter.recipients_excel)

    json_collection = []

    counter = 1
    for result in unique_results:
        json_object = {}
        json_object["id"] = counter
        json_object["label"] = result
        json_object["count"] = categorized_letters[result]
        json_collection.append(json_object)
        counter += 1

    data = json.dumps(json_collection)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
