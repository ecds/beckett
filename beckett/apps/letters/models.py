from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person, Organization
from beckett.apps.geo.models import Place
from beckett.apps.works.models import Work


class Letter(models.Model):
    'Letters sent by Samuel Beckett'

    year = models.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2000)])
    month = models.IntegerField(blank=True, validators=[MinValueValidator(1),MaxValueValidator(12)])
    day = models.IntegerField(blank=True, validators=[MinValueValidator(1),MaxValueValidator(31)])

    physical_description = models.CharField(max_length=255, blank=True, null=True)
    leaves_sides = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    postmark = models.CharField(max_length=255, blank=True, null=True)

    recipients_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    recipients = models.ManyToManyField(Person, blank=True)

    people_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    people = models.ManyToManyField(Person, blank=True, related_name='+', help_text="People mentioned in letter")

    publishers_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    publishers = models.ManyToManyField(Organization, blank=True, help_text="Publishers/agents/producers mentioned in letter")

    places_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    places = models.ManyToManyField(Place, blank=True, help_text="Places mentioned in letter")

    sb_writing_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    sb_writing = models.ManyToManyField(Work, blank=True, related_name='sb_writing', help_text="SB writing referenced in letter")

    sb_publications_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    sb_publications = models.ManyToManyField(Work, blank=True, related_name='sb_publications', help_text="Publications of SB's work referenced in letter")

    sb_productions_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    sb_productions = models.ManyToManyField(Work, blank=True, related_name='sb_productions', help_text="Productions of SB's work referenced in letter")

    self_translations_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    self_translations = models.ManyToManyField(Work, blank=True, related_name='self_translations', help_text="Self-translation and translation by SB referenced in letter")

    translations_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    translations = models.ManyToManyField(Work, blank=True, related_name='translations', help_text="Translation's SB's work referenced in letter")

    sb_reading_input = tinymce_models.HTMLField(blank=True, help_text="Input from Excel database")
    sb_reading = models.ManyToManyField(Work, blank=True, related_name='sb_reading', help_text="SB's reading referenced in letter")

    key_terms = tinymce_models.HTMLField(blank=True)
    events_attended = tinymce_models.HTMLField(blank=True)
    sports = tinymce_models.HTMLField(blank=True)
    censorship = tinymce_models.HTMLField(blank=True)
    sb_health = tinymce_models.HTMLField(blank=True)

    def recipient_list(self):
        return "; ".join(['%s %s' % (r.first_name, r.last_name) for r in self.recipients.all()])



