from django.contrib import admin

from beckett.apps.events.models import Chronology

class ChronologyAdmin(admin.ModelAdmin):
    list_display = ['year', 'label', 'description']
    search_fields = ['year', 'label', 'description']
    

admin.site.register(Chronology, ChronologyAdmin)