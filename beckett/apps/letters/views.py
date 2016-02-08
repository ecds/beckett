from django.shortcuts import render
from django.views.generic import ListView
from beckett.apps.letters.models import Letter
from django.template import RequestContext
from beckett.apps.letters.forms import LetterSearchForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response

class LettersList(ListView):
    model = Letter


def searchbox(request):
    "Search letters by title/author/keyword"
    form = LetterSearchForm(request.GET)
    response_code = None
    context = {'searchbox': form}
    search_opts = {}
    number_of_results = 20
      
    if form.is_valid():
        if 'keyword' in form.cleaned_data and form.cleaned_data['keyword']:
            search_opts['primary_language'] = '%s' % form.cleaned_data['keyword']
                
        letters = Letter.objects.only('id', 'primary_language', 'year', 'month', 'day').filter(**search_opts)

        searchbox_paginator = Paginator(letters, number_of_results)
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        # If page request (9999) is out of range, deliver last page of results.
        try:
            searchbox_page = searchbox_paginator.page(page)
        except (EmptyPage, InvalidPage):
            searchbox_page = searchbox_paginator.page(paginator.num_pages)

        context['letters'] = letters
        context['letters_paginated'] = searchbox_page
        context['keyword'] = form.cleaned_data['keyword']
           
        response = render_to_response('search_results.html', context, context_instance=RequestContext(request))
    #no search conducted yet, default form
        
    else:
        response = render(request, 'search.html', {"searchbox": form}, context_instance=RequestContext(request))
       
    if response_code is not None:
        response.status_code = response_code
    return response



def letter_display(request, doc_id):
    "Display the contents of a single letter."
    if 'keyword' in request.GET:
        search_terms = request.GET['keyword']
        url_params = '?' + urlencode({'keyword': search_terms})
        filter = {'highlight': search_terms}    
    else:
        url_params = ''
        filter = {}
        search_terms = None
    try:              
        letter = Letter.objects.filter(**filter).get(id__exact=doc_id)
        format = letter.xsl_transform(filename=os.path.join(settings.BASE_DIR, '..', 'yjallen_app', 'xslt', 'form.xsl'))
        return render_to_response('letter_display.html', {'letter': letter, 'format': format.serialize(), 'search_terms': search_terms}, context_instance=RequestContext(request))
    except DoesNotExist:
        raise Http404