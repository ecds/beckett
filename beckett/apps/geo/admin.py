from django.contrib import admin

from beckett.apps.geo.models import Place, Repository

class PlaceAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/collapseTabularInlines.js',)
        css = { 'all' : ('css/admin/admin_styles.css',) }

    list_display = ['street_address', 'city', 'state', 'zipcode', 'country']
    list_display_links = ['street_address', 'city', 'state', 'zipcode', 'country']
    search_fields = ['street_address', 'city', 'state',
                     'zipcode', 'country',
                     'Latitude', 'Longitude']
    inlines = [
        
    ]

class RepositoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abb', 'descriptive_information', 'storage_information', 'street_address', 'city', 'country']
    search_fields = ['name', 'descriptive_information', 'storage_information', 
                     'street_address', 'city', 'state',
                     'zipcode', 'country',
                     'Latitude', 'Longitude']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Repository, RepositoryAdmin)