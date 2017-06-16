from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person, Organization
from beckett.apps.geo.models import Place, Repository
from beckett.apps.works.models import Production, Publication, Writing, Directing, Translating
from django.utils.html import format_html


class Letter(models.Model):
    'Letters sent by Samuel Beckett'

    'Basic Info'
    letter_code = models.CharField(max_length=100, primary_key=True)
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(2000)])
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(12)])
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(31)])
    primary_language = models.CharField(max_length=255, blank=True, null=True)

    physical_description = models.CharField(max_length=255, blank=True, null=True)
    leaves_sides = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    postmark = models.CharField(max_length=255, blank=True, null=True)
    place_written = models.CharField(max_length=255, blank=True, null=True)
    place_sent = models.CharField(max_length=255, blank=True, null=True)
    recipients_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    recipients = models.ManyToManyField(Person, blank=True, related_name='recipients')
    repository_excel = tinymce_models.HTMLField(blank=True, null=True, help_text="excel from Excel database")
    repository = models.ManyToManyField(Repository, blank=True)

 
    'Linked Data Fields'
    people = models.ManyToManyField(Person, blank=True, related_name='manypeople')
    places = models.ManyToManyField(Place, blank=True, related_name='manyplaces')
    organizations = models.ManyToManyField(Organization, blank=True, related_name='manyorganizations')
    productions = models.ManyToManyField(Production, blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    directing = models.ManyToManyField(Directing, blank=True)
    writing = models.ManyToManyField(Writing, blank=True)
    translating = models.ManyToManyField(Translating, blank=True)





    
    def recipient_list(self):
        return "; ".join(['%s %s' % (r.first_name, r.last_name) for r in self.recipients.all()])

    def recipients_html(self):
        return format_html(self.recipients_excel)

    class Meta: 
        ordering = ['year', 'month', 'day']