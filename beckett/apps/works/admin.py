from django.contrib import admin

from beckett.apps.works.models import Work, Edition



class EditionInline(admin.TabularInline):
    model = Edition
    verbose_name_plural = "Editions"
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    filter_horizontal = ['authors']
    inlines = [
        EditionInline,
    ]

admin.site.register(Work, WorkAdmin)
