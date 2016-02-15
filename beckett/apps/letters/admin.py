from django.contrib import admin

from beckett.apps.letters.models import Letter

  

class LetterAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/collapseTabularInlines.js',)
        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['year', 'month', 'day', 'recipient_list', 'recipients_input', 'primary_language']
    filter_horizontal = ['recipients', 
                         'people', 
                         'publishers', 
                         'places', 
                         'sb_writing', 
                         'sb_publications', 
                         'sb_productions', 
                         'self_translations',
                         'translations',
                         'sb_reading',
                         'repository']
    fieldsets = (
        (None, {
            'fields': ('year', 'month', 'day', 'primary_language')}),
        ('Recipients', {
            'classes': ('collapse',),
            'fields': ('recipients_input', 'recipients')}),
        ('Physical Description', {
            'classes': ('collapse',),
            'fields': ('physical_description', 'leaves_sides', 'envelope', 'postmark')}),
        ('Key Terms', {
            'classes': ('collapse',),
            'fields': ('key_terms',)}),
        ('People', {
            'classes': ('collapse',),
            'fields': ('people_input', 'people')}),
        ('Publishers/Agents/Producers', {
            'classes': ('collapse',),
            'fields': ('publishers_input', 'publishers')}),
        ('Repository Information', {
            'classes': ('collapse',),
            'fields': ('repository_input', 'repository', 'owner_input')}),
        ('Places', {
            'classes': ('collapse',),
            'fields': ('places_input', 'places', 'place_written_input', 'place_written', 'place_sent_input', 'place_sent')}),
        ('SB Writing', {
            'classes': ('collapse',),
            'fields': ('sb_writing_input', 'sb_writing')}),
        ('SB Publications and Productions', {
            'classes': ('collapse',),
            'fields': ('sb_publications_input', 'sb_publications', 'edition_notes', 'sb_productions_input', 'sb_productions', 'edition_notes2')}),
        ('Translations', {
            'classes': ('collapse',),
            'fields': ('self_translations_input','self_translations','edition_notes3', 'translations_input','translations', 'edition_notes4')}),
        ('Censorship', {
            'classes': ('collapse',),
            'fields': ('censorship',)}),
        ('Publication Information', {
            'classes': ('collapse',),
            'fields': ('publication', 'volume','previous_publication', 'place_of_previous_publication',)}),
        ('SB Reading', {
            'classes': ('collapse',),
            'fields': ('sb_reading_input', 'sb_reading')}),
        ('SB Activities', {
            'classes': ('collapse',),
            'fields': ('events_attended','sports','sb_health')}),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('additional_information',)}),
    )
    search_fields = ('year', 'primary_language', 'recipients_input', 'physical_description', 'leaves_sides', 'envelope', 'postmark', 'places_input', 'place_written_input', 'place_sent_input', 'additional_information', 'events_attended','sports','sb_health','self_translations_input','translations_input', 'sb_publications_input', 'sb_writing_input', 'sb_productions_input')

admin.site.register(Letter, LetterAdmin)