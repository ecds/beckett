from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.letters.models import Letter
from django.template import RequestContext
from beckett.apps.letters.forms import LetterSearchForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

class LettersList(ListView):
    model = Letter

class LettersDetail(DetailView):
    model = Letter
    queryset = Letter.objects.all()
    template_name = 'letters/letter_detail.html'

#def searchbox(request):
#    "Search letters"
#    form = LetterSearchForm(request.GET)
#    response_code = None
#    context = {'searchbox': form}
#    search_opts = {}
#    number_of_results = 20
#      
#    if form.is_valid():
#        if 'keyword' in form.cleaned_data and form.cleaned_data['keyword']:
#            search_opts['primary_language'] = '%s' % form.cleaned_data['keyword']
#                
#        letters = Letter.objects.only("id", "primary_language", "year", "month", "day", "key_terms").filter(**search_opts)
#
#        searchbox_paginator = Paginator(letters, number_of_results)
#        
#        try:
#            page = int(request.GET.get('page', '1'))
#        except ValueError:
#            page = 1
#        # If page request (9999) is out of range, deliver last page of results.
#        try:
#            searchbox_page = searchbox_paginator.page(page)
#        except (EmptyPage, InvalidPage):
#            searchbox_page = searchbox_paginator.page(paginator.num_pages)
#
#        context['letters'] = letters
#        context['letters_paginated'] = searchbox_page
#        context['keyword'] = form.cleaned_data['keyword']
#           
#        response = render_to_response('search_results.html', context, context_instance=RequestContext(request))
#    #no search conducted yet, default form
#        
#    else:
#        response = render(request, 'search.html', {"searchbox": form}, context_instance=RequestContext(request))
#       
#    if response_code is not None:
#        response.status_code = response_code
#    return response


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
    
    
    
#def searchtext(request):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        key_terms = Letter.objects.all()
#        return render(request, 'search_results.html',
#            {'key_terms': key_terms, 'query': q})
#    else:
#        return HttpResponse('Please submit a search term.')
    


#def letter_display(request, doc_id):
#    "Display the contents of a single letter."
#    if 'keyword' in request.GET:
#        search_terms = request.GET['keyword']
#        url_params = '?' + urlencode({'keyword': search_terms})
#        filter = {'highlight': search_terms}    
#    else:
#        url_params = ''
#        filter = {}
#        search_terms = None
#    try:              
#        letter = Letter.objects.filter(**filter).get(id__exact=doc_id)
#        format = letter.xsl_transform(filename=os.path.join(settings.BASE_DIR, '..', 'yjallen_app', 'xslt', 'form.xsl'))
#        return render_to_response('letter_display.html', {'letter': letter, 'format': format.serialize(), 'search_terms': search_terms}, context_instance=RequestContext(request))
#    except DoesNotExist:
#        raise Http404