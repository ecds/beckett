from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person, Organization
from beckett.apps.geo.models import Place, Repository
from beckett.apps.works.models import Work
from django.utils.html import format_html


class Letter(models.Model):
    'Letters sent by Samuel Beckett'

    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(2000)])
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(31)])
    primary_language = models.CharField(max_length=255, blank=True, null=True)

    physical_description = models.CharField(max_length=255, blank=True, null=True)
    leaves_sides = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    postmark = models.CharField(max_length=255, blank=True, null=True)

    recipients_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    recipients = models.ManyToManyField(Person, blank=True, related_name='recipients')

    people_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name=u"People mentioned excel", help_text="excel from Excel database")
    people = models.ManyToManyField(Person, verbose_name=u"People mentioned", blank=True, related_name='manypeople', help_text="People mentioned in letter")

    publishers_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    publishers = models.ManyToManyField(Organization, blank=True, help_text="Publishers/agents/producers mentioned in letter")

    repository_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    repository = models.ManyToManyField(Repository, blank=True, related_name="placeofkeeping", help_text="Repository")
    owner_excel =  tinymce_models.HTMLField(blank=True, null=True, help_text="excel OwnerProp from Excel database")
    places_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name="Places mentioned excel", help_text="excel from Excel database")
    places = models.ManyToManyField(Place, blank=True, verbose_name="Places mentioned", related_name='mentioned', help_text="Places mentioned in letter")
    place_written_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    place_written = models.ForeignKey(Place, blank=True, null=True, related_name='written', help_text="Place where the letter was written")
    place_sent_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    place_sent = models.ForeignKey(Place, blank=True, null=True, related_name='sent', help_text="Place to which the letter was sent")

    sb_writing_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name="SB writing excel", help_text="excel from Excel database")
    sb_writing = models.ManyToManyField(Work, blank=True, verbose_name="SB writing", related_name='sb_writing', help_text="SB writing referenced in letter")

    sb_publications_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name="SB publications excel", help_text="excel from Excel database")
    sb_publications = models.ManyToManyField(Work, blank=True, verbose_name="SB publications", related_name='sb_publications', help_text="Publications of SB's work referenced in letter")
    edition_notes = models.CharField(max_length=255, blank=True, null=True, verbose_name="Publication edition notes")
    sb_productions_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name="SB productions excel", help_text="excel from Excel database")
    sb_productions = models.ManyToManyField(Work, blank=True, verbose_name="SB productions", related_name='sb_productions', help_text="Productions of SB's work referenced in letter")
    edition_notes2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production version notes")

    self_translations_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    self_translations = models.ManyToManyField(Work, blank=True, related_name='self_translations', help_text="Self-translation and translation by SB referenced in letter")
    edition_notes3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Self-translation edition notes")

    translations_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    translations = models.ManyToManyField(Work, blank=True, related_name='translations', help_text="Translation's SB's work referenced in letter")
    edition_notes4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Translation edition notes")

    publication = models.NullBooleanField(blank=True, null=True, help_text="Was it in a publication?")
    volume = models.CharField(max_length=255, blank=True, null=True)
    previous_publication = models.NullBooleanField(blank=True, null=True, help_text="Was there a previous publication?")
    place_of_previous_publication = models.ForeignKey(Place, blank=True, null=True, related_name='publication', help_text="Place of Previous Publication")

    sb_reading_excel = tinymce_models.HTMLField(blank=True, null=True, verbose_name="SB reading excel", help_text="excel from Excel database")
    sb_reading = models.ManyToManyField(Work, blank=True, verbose_name="SB reading", related_name='sb_reading', help_text="SB's reading referenced in letter")

    key_terms = tinymce_models.HTMLField(null=True, blank=True)
    events_attended = tinymce_models.HTMLField(null=True, blank=True)
    sports = tinymce_models.HTMLField(null=True, blank=True)
    censorship = tinymce_models.HTMLField(null=True, blank=True)
    sb_health = tinymce_models.HTMLField(null=True, blank=True, verbose_name="SB health mentioned")
    additional_information = tinymce_models.HTMLField(null=True, blank=True)
    
    def recipient_list(self):
        return "; ".join(['%s %s' % (r.first_name, r.last_name) for r in self.recipients.all()])

    def recipients_html(self):
        return format_html(self.recipients_excel)

    class Meta: 
        ordering = ['year', 'month', 'day']