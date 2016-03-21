from django.contrib import admin

from beckett.apps.letters.models import Letter
from django.utils.html import format_html

  

class LetterAdmin(admin.ModelAdmin):
#    class Media:
#        js = ('js/admin/collapseTabularInlines.js',)
#        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['year', 'month', 'day', 'recipient_list', 'recipients_html', 'primary_language']
    filter_horizontal = ('recipients', 'people', 'publishers', 'places', 'sb_writing', 'sb_publications','sb_productions', 'self_translations', 'translations', 'sb_reading', 'repository')
    fieldsets = (
        (None, {
            'fields': ('year', 'month', 'day', 'primary_language')}),
        ('Recipients', {
            'classes': ('collapse',),
            'fields': ('recipients', 'recipients_excel')}),
        ('Physical Description', {
            'classes': ('collapse',),
            'fields': ('physical_description', 'leaves_sides', 'envelope', 'postmark')}),
        ('Key Terms', {
            'classes': ('collapse',),
            'fields': ('key_terms',)}),
        ('People Mentioned', {
            'classes': ('collapse',),
            'fields': ('people', 'people_excel')}),
        ('Publishers/Agents/Producers', {
            'classes': ('collapse',),
            'fields': ('publishers', 'publishers_excel')}),
        ('Repositories', {
            'classes': ('collapse',),
            'fields': ('repository', 'repository_excel', 'owner_excel')}),
        ('Places', {
            'classes': ('collapse',),
            'fields': ('places', 'places_excel', 'place_written', 'place_written_excel', 'place_sent', 'place_sent_excel')}),
        ('SB Writing', {
            'classes': ('collapse',),
            'fields': ('sb_writing', 'sb_writing_excel')}),
        ('SB Publications and Productions', {
            'classes': ('collapse',),
            'fields': ('sb_publications', 'sb_publications_excel', 'edition_notes', 'sb_productions', 'sb_productions_excel', 'edition_notes2')}),
        ('Translations', {
            'classes': ('collapse',),
            'fields': ('self_translations','self_translations_excel','edition_notes3','translations', 'translations_excel', 'edition_notes4')}),
        ('Censorship', {
            'classes': ('collapse',),
            'fields': ('censorship',)}),
        ('Publication Information', {
            'classes': ('collapse',),
            'fields': ('publication', 'volume','previous_publication', 'place_of_previous_publication',)}),
        ('SB Reading', {
            'classes': ('collapse',),
            'fields': ('sb_reading', 'sb_reading_excel')}),
        ('SB Activities', {
            'classes': ('collapse',),
            'fields': ('events_attended','sports','sb_health')}),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('additional_information',)}),
    )
    search_fields = ('year', 'primary_language', 'recipients_excel', 'physical_description', 'leaves_sides', 'envelope', 'postmark', 'places_excel', 'place_written_excel', 'place_sent_excel', 'additional_information', 'events_attended','sports','sb_health','self_translations_excel','translations_excel', 'sb_publications_excel', 'sb_writing_excel', 'sb_productions_excel')

admin.site.register(Letter, LetterAdmin)