from django.contrib import admin

from beckett.apps.letters.models import Letter
from django.utils.html import format_html

  

class LetterAdmin(admin.ModelAdmin):
#    class Media:
#        js = ('js/admin/collapseTabularInlines.js',)
#        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['reg_recipient', 'year', 'month', 'day']
    filter_horizontal = ['repository_linked', 'recipients', 'people', 'places', 'organizations', 'productions', 'publications', 'directing', 'writing', 'translating', 'reading', 'attendance', 'public_events']

admin.site.register(Letter, LetterAdmin)