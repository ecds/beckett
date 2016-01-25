from django.contrib import admin

from beckett.apps.geo.models import Place, Repository

class PlaceAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/collapseTabularInlines.js',)
        css = { 'all' : ('css/admin/admin_styles.css',) }

    list_display = ['street_address', 'city', 'state', 'zipcode', 'country']
    list_display_links = ['street_address', 'city', 'state', 'zipcode', 'country']
    search_fields = ['street_address', 'city', 'state__name', 'state__code',
                     'zipcode', 'country__name', 'country__code',
                     'placename__name', 'placename__item__title']
    inlines = [
        
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Repository)