from django.contrib import admin

from beckett.apps.works.models import Production, Publication, Directing, Translating, Writing, Reading



class ProductionAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title', 'director']
    search_fields = ['title', 'director', 'theatre', 'city', 'date', 'actors']

admin.site.register(Production, ProductionAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title', 'translator']
    search_fields = ['title', 'translator', 'place_pub_date']

admin.site.register(Publication, PublicationAdmin)


class WritingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title', 'authors']
    search_fields = ['title', 'authors']

admin.site.register(Writing, WritingAdmin)


class DirectingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'title', 'authors']
    search_fields = ['title', 'authors']

admin.site.register(Directing, DirectingAdmin)


class TranslatingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'work', 'language']
    search_fields = ['title', 'translator', 'translated_title']

admin.site.register(Translating, TranslatingAdmin)

class ReadingAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'book', 'author']
    search_fields = ['author', 'book', 'publication']

admin.site.register(Reading, ReadingAdmin)