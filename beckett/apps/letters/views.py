from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.letters.models import Letter
from beckett.apps.people.models import Person, Organization
from beckett.apps.geo.models import Place
from beckett.apps.works.models import Production, Publication, Writing, Directing, Translating, Reading
from beckett.apps.events.models import Public_event, Attendance
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

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for person in people:
                profile_ids.append(person.profile_id)

            letter_list = letter_list.filter(people__profile_id__in=profile_ids)

        if field == "places_mentioned":
            places = Place.objects.filter(name__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for place in places:
                profile_ids.append(place.profile_id)

            letter_list = letter_list.filter(places__profile_id__in=profile_ids)

        if field == "organizations":
            organizations = Organization.objects.filter(name__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for org in organizations:
                profile_ids.append(org.profile_id)

            letter_list = letter_list.filter(organizations__profile_id__in=profile_ids)

        if field == "productions":
            productions = Production.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for production in productions:
                profile_ids.append(production.profile_id)

            letter_list = letter_list.filter(productions__profile_id__in=profile_ids)

        if field == "publications":
            publications = Publication.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for publication in publications:
                profile_ids.append(publication.profile_id)

            letter_list = letter_list.filter(publications__profile_id__in=profile_ids)

        if field == "directing":
            directing = Directing.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for d in directing:
                profile_ids.append(d.profile_id)

            letter_list = letter_list.filter(directing__profile_id__in=profile_ids)

        if field == "writing":
            writing = Writing.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for w in writing:
                profile_ids.append(w.profile_id)

            letter_list = letter_list.filter(writing__profile_id__in=profile_ids)

        if field == "translating":
            translating = Translating.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for t in translating:
                profile_ids.append(t.profile_id)

            letter_list = letter_list.filter(translating__profile_id__in=profile_ids)

        if field == "reading":
            reading = Reading.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for r in reading:
                profile_ids.append(r.profile_id)

            letter_list = letter_list.filter(reading__profile_id__in=profile_ids)

        if field == "attendance":
            attendance = Attendance.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for a in attendance:
                profile_ids.append(a.profile_id)

            letter_list = letter_list.filter(attendance__profile_id__in=profile_ids)

        if field == "public_events":
            public_events = Public_event.objects.filter(title__icontains = query)

            profile_ids = [] # Colleciton of profile_ids that are of interest
            for event in public_events:
                profile_ids.append(event.profile_id)

            letter_list = letter_list.filter(public_events__profile_id__in=profile_ids)

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

    if field == "places_mentioned":

        places = Place.objects.filter(name__icontains = q)

        for place in places:
            letters = Letter.objects.filter(places__profile_id = place.profile_id)
            for letter in letters:
                results.append(place.name)
        categorized_letters = Counter(results)
        for place in places:
            letters = Letter.objects.filter(places__profile_id = place.profile_id)
            for letter in letters:
                if place.name not in unique_results:
                    unique_results.append(place.name)


    if field == "organizations":

        organizations = Organization.objects.filter(name__icontains = q)

        for org in organizations:
            letters = Letter.objects.filter(organizations__profile_id = org.profile_id)
            for letter in letters:
                results.append(org.name)
        categorized_letters = Counter(results)
        for org in organizations:
            letters = Letter.objects.filter(organizations__profile_id = org.profile_id)
            for letter in letters:
                if org.name not in unique_results:
                    unique_results.append(org.name)


    if field == "productions":

        productions = Production.objects.filter(title__icontains = q)

        for production in productions:
            letters = Letter.objects.filter(productions__profile_id = production.profile_id)
            for letter in letters:
                results.append(production.title)
        categorized_letters = Counter(results)
        for production in productions:
            letters = Letter.objects.filter(productions__profile_id = production.profile_id)
            for letter in letters:
                if production.title not in unique_results:
                    unique_results.append(production.title)

    if field == "publications":

        publications = Production.objects.filter(title__icontains = q)

        for publication in publications:
            letters = Letter.objects.filter(publications__profile_id = publication.profile_id)
            for letter in letters:
                results.append(publication.title)
        categorized_letters = Counter(results)
        for publication in publications:
            letters = Letter.objects.filter(publications__profile_id = publication.profile_id)
            for letter in letters:
                if publication.title not in unique_results:
                    unique_results.append(publication.title)

    if field == "directing":

        directing = Directing.objects.filter(title__icontains = q)

        for d in directing:
            letters = Letter.objects.filter(directing__profile_id = d.profile_id)
            for letter in letters:
                results.append(d.title)
        categorized_letters = Counter(results)
        for d in directing:
            letters = Letter.objects.filter(directing__profile_id = d.profile_id)
            for letter in letters:
                if d.title not in unique_results:
                    unique_results.append(d.title)

    if field == "writing":

        writing = Writing.objects.filter(title__icontains = q)

        for w in writing:
            letters = Letter.objects.filter(writing__profile_id = w.profile_id)
            for letter in letters:
                results.append(w.title)
        categorized_letters = Counter(results)
        for w in writing:
            letters = Letter.objects.filter(writing__profile_id = w.profile_id)
            for letter in letters:
                if w.title not in unique_results:
                    unique_results.append(w.title)

    if field == "translating":

        translating = Translating.objects.filter(title__icontains = q)

        for t in translating:
            letters = Letter.objects.filter(translating__profile_id = t.profile_id)
            for letter in letters:
                results.append(t.title)
        categorized_letters = Counter(results)
        for t in translating:
            letters = Letter.objects.filter(translating__profile_id = t.profile_id)
            for letter in letters:
                if t.title not in unique_results:
                    unique_results.append(t.title)

    if field == "reading":

        reading = Reading.objects.filter(title__icontains = q)

        for r in reading:
            letters = Letter.objects.filter(reading__profile_id = r.profile_id)
            for letter in letters:
                results.append(r.title)
        categorized_letters = Counter(results)
        for r in reading:
            letters = Letter.objects.filter(reading__profile_id = r.profile_id)
            for letter in letters:
                if r.title not in unique_results:
                    unique_results.append(r.title)

    if field == "attendance":

        attendance = Attendance.objects.filter(title__icontains = q)

        for a in attendance:
            letters = Letter.objects.filter(attendance__profile_id = a.profile_id)
            for letter in letters:
                results.append(a.title)
        categorized_letters = Counter(results)
        for a in attendance:
            letters = Letter.objects.filter(attendance__profile_id = a.profile_id)
            for letter in letters:
                if a.title not in unique_results:
                    unique_results.append(a.title)

    if field == "public_events":

        public_events = Public_event.objects.filter(title__icontains = q)

        for event in public_events:
            letters = Letter.objects.filter(public_events__profile_id = event.profile_id)
            for letter in letters:
                results.append(event.title)
        categorized_letters = Counter(results)
        for event in public_events:
            letters = Letter.objects.filter(public_events__profile_id = event.profile_id)
            for letter in letters:
                if event.title not in unique_results:
                    unique_results.append(event.title)


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
