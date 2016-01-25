from django.contrib import admin

from beckett.apps.works.models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Work, WorkAdmin)
