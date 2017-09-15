from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.letters.models import Letter
from beckett.apps.people.models import Person
from django.template import RequestContext
from beckett.apps.letters.forms import LetterSearchForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db.models import Q
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

def search(request):
    query = request.GET.get("q")
    field = request.GET.get("field")

    letter_list = Letter.objects.all()

    if query:
        if field == "recipients":
            letter_list = letter_list.filter(recipients_excel__icontains=query)
        if field == "place_sent":
            letter_list = letter_list.filter(place_sent__icontains=query)
        if field == "repository":
            letter_list = letter_list.filter(repository_excel__icontains=query)
        # if field == "people":
        #     letter_list = letter_list.filter(Q(people__last_name__icontains = query)| Q(people__first_name__icontains = query))
        if field == "people":
            query  = query.split(' ')
            first_name = query[0]
            last_name = query[1]
            people = Person.objects.filter(last_name__icontains = last_name,
        first_name__icontains = first_name)
            for person in people:
                letters = letter_list.filter(people__profile_id = person.profile_id)

            

    context = {
        "letter_list": letter_list,
        "request": request,
        "result_count": len(letter_list)
    }

    return render(request, 'search.html', context)

# An API method that returns a JSON with filtered recipients and corresponding
# occurrence count. This is consumed by select2 in the search filter to
# fulfill autocomplete feature requirement
def get_search_autocomplete(request):
    q = request.GET.get('term')
    field = request.GET.get('field')
    letters = []
    results = []
    unique_results = []

    if field == "recipients":
        letters = Letter.objects.filter(recipients_excel__icontains = q)
        for letter in letters:
            results.append(letter.recipients_excel)
        categorized_letters = Counter(results)
        for letter in letters:
            if letter.recipients_excel not in unique_results:
                unique_results.append(letter.recipients_excel)

    if field == "place_sent":
        letters = Letter.objects.filter(place_sent__icontains = q)
        for letter in letters:
            results.append(letter.place_sent)
        categorized_letters = Counter(results)
        for letter in letters:
            if letter.place_sent not in unique_results:
                unique_results.append(letter.place_sent)

    if field == "repository":
        letters = Letter.objects.filter(repository_excel__icontains = q)
        for letter in letters:
            results.append(letter.repository_excel)
        categorized_letters = Counter(results)
        for letter in letters:
            if letter.repository_excel not in unique_results:
                unique_results.append(letter.repository_excel)

    if field == "people":

        people = Person.objects.filter(Q(last_name__icontains = q)|
        Q(first_name__icontains = q))  

        for person in people:
            name  = person.first_name + ' ' + person.last_name
            letters = Letter.objects.filter(people__profile_id = person.profile_id)
            for letter in letters:
                results.append(name)
        categorized_letters = Counter(results)
        for person in people:
            name  = person.first_name + ' ' + person.last_name
            letters = Letter.objects.filter(people__profile_id = person.profile_id)
            for letter in letters:
                if name not in unique_results:
                    unique_results.append(name)



        # for letter in letters:
        #     people = Person.objects.filter(manypeople__letter_code = letter.letter_code)
        #     for person in people:
        #         results.append((person.first_name + ' ' + person.last_name))
        # categorized_letters = Counter(results)
        # for letter in letters:
        #     people = Person.objects.filter(manypeople__letter_code = letter.letter_code)
        #     for person in people:
        #         if person not in unique_results:
        #             unique_results.append((person.first_name + ' ' + person.last_name))

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
