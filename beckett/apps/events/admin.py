from django.contrib import admin

from beckett.apps.events.models import Chronology, EventResource, Attendance, Public_event

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


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'thing', 'title']
    search_fields = ['thing', 'title', 'place_date', 'attends_with']

admin.site.register(Attendance, AttendanceAdmin)



class Public_eventAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'event', 'date']
    search_fields = ['event']

admin.site.register(Public_event, Public_eventAdmin)