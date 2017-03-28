from django.contrib import admin

from beckett.apps.letters.models import Letter
from django.utils.html import format_html

  

class LetterAdmin(admin.ModelAdmin):
#    class Media:
#        js = ('js/admin/collapseTabularInlines.js',)
#        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['year', 'month', 'day', 'recipient_list', 'recipients_html', 'primary_language']

admin.site.register(Letter, LetterAdmin)