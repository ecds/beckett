from django.contrib import admin
from django.utils.html import format_html

# from beckett.apps.letters.models import Letter
from beckett.apps.people.models import Person, Name, PenName


class AltNamesInline(admin.TabularInline):
    model = Name
    verbose_name_plural = 'Alternate Names'
    extra = 1

class PenNamesInline(admin.TabularInline):
    model = PenName
    verbose_name_plural = 'Pen Names'
    extra = 1

# class LetterInline(admin.TabularInline):
#     model = Letter.persons_mentioned.through
#     extra = 0
#     verbose_name = 'Mentioned In Letters'
#     verbose_name_plural = verbose_name
#     exclude = ('letter', )
#     readonly_fields = ('edit_letter', )

#     can_delete = False

#     def edit_letter(self, obj):
#         # creator name is edited on issue item
#         return format_html(u'<a href="{}">{}</a>',
#             obj.item.edit_url, obj.item.title)

#     edit_item.short_description = "Item"

#     def has_add_permission(self, args):
#         # disallow adding mentions from the Person edit form
#         return False


# class ItemCreatorsInline(admin.TabularInline):
#     model = Item.creators.through
#     extra = 0
#     verbose_name = 'Assigned Creator for Items'
#     verbose_name_plural = verbose_name
#     exclude = ('issue_item', )
#     readonly_fields = ('edit_item', 'name_used')
#     can_delete = False

#     def edit_item(self, obj):
#         # creator name is edited on issue item
#         return format_html(u'<a href="{}">{}</a>',
#             obj.item.edit_url, obj.item.title)

#     edit_item.short_description = "Item"

#     def has_add_permission(self, args):
#         # disallow adding creator names from the Person edit form
#         return False


class PersonAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/collapseTabularInlines.js',)
        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['first_name', 'last_name', 'gender', 'uri']
    search_fields = ['first_name', 'last_name', 'gender', 'notes', 'uri']
    list_display_links = ['first_name', 'last_name']
    inlines = [
        AltNamesInline,
        PenNamesInline,
        # LetterInline,
        # ItemCreatorsInline,
    ]

admin.site.register(Person, PersonAdmin)