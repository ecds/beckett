from django.contrib import admin

from beckett.apps.events.models import Chronology, EventResource

class EventResourceInline(admin.TabularInline):
    model = EventResource
    verbose_name_plural = 'Event Resources'
    extra = 1

class ChronologyAdmin(admin.ModelAdmin):
    list_display = ['year', 'label']
    search_fields = ['year', 'label', 'description']
    inlines = [
        EventResourceInline,
    ]


admin.site.register(Chronology, ChronologyAdmin)