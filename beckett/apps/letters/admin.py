from django.contrib import admin

from beckett.apps.letters.models import Letter

  

class LetterAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/collapseTabularInlines.js',)
        css = { 'all' : ('css/admin/admin_styles.css',) }
    list_display = ['year', 'month', 'day', 'recipient_list']
    filter_horizontal = ['recipients', 
                         'people', 
                         'publishers', 
                         'places', 
                         'sb_writing', 
                         'sb_publications', 
                         'sb_productions', 
                         'self_translations',
                         'translations',
                         'sb_reading']
    fieldsets = (
        (None, {
            'fields': ('year', 'month', 'day')}),
        ('Physical Description', {
            'classes': ('collapse',),
            'fields': ('physical_description', 'leaves_sides', 'envelope', 'postmark')}),
        ('Recipients', {
            'classes': ('collapse',),
            'fields': ('recipients_input', 'recipients')}),
        ('Key Terms', {
            'classes': ('collapse',),
            'fields': ('key_terms',)}),
        ('People', {
            'classes': ('collapse',),
            'fields': ('people_input', 'people')}),
        ('Publishers/Agents/Producers', {
            'classes': ('collapse',),
            'fields': ('publishers_input', 'publishers')}),
        ('Places', {
            'classes': ('collapse',),
            'fields': ('places_input', 'places')}),
        ('SB Writing', {
            'classes': ('collapse',),
            'fields': ('sb_writing_input', 'sb_writing')}),
        ('SB Publications', {
            'classes': ('collapse',),
            'fields': ('sb_publications_input', 'sb_publications')}),
        ('SB Productions', {
            'classes': ('collapse',),
            'fields': ('sb_productions_input', 'sb_productions')}),
        ('Self-Translations', {
            'classes': ('collapse',),
            'fields': ('self_translations_input','self_translations')}),
        ('Translations', {
            'classes': ('collapse',),
            'fields': ('translations_input','translations')}),
        ('SB Reading', {
            'classes': ('collapse',),
            'fields': ('sb_reading_input', 'sb_reading')}),
        ('Events Attended', {
            'classes': ('collapse',),
            'fields': ('events_attended',)}),
        ('Sports', {
            'classes': ('collapse',),
            'fields': ('sports',)}),
        ('Censorship', {
            'classes': ('collapse',),
            'fields': ('censorship',)}),
        ('SB Health', {
            'classes': ('collapse',),
            'fields': ('sb_health',)}),
    )


admin.site.register(Letter, LetterAdmin)