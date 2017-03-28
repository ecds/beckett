from django.contrib import admin

from beckett.apps.works.models import Production, Publication, Directing, Translating, Writing



class ProductionAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Production, ProductionAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Publication, PublicationAdmin)


class WritingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Writing, WritingAdmin)


class DirectingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Directing, DirectingAdmin)


class TranslatingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title']
    search_fields = ['title']
    filter_horizontal = ['authors']

admin.site.register(Translating, TranslatingAdmin)