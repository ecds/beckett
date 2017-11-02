from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person, Organization
from beckett.apps.geo.models import Place, Repository
from beckett.apps.works.models import Production, Publication, Writing, Directing, Translating, Reading
from beckett.apps.events.models import Attendance, Public_event 
from django.utils.html import format_html


class Letter(models.Model):
    'Letters sent by Samuel Beckett'

    'Big Sam'
    id = models.IntegerField(primary_key=True)
    letter_code = models.CharField(max_length=100, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(31)])
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(12)])
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(2000)])
    addressed_from_actual = models.CharField(max_length=255, blank=True, null=True)
    reg_place_written = models.CharField(max_length=255, blank=True, null=True)
    reg_place_written_city = models.CharField(max_length=255, blank=True, null=True)
    reg_place_written_country = models.CharField(max_length=255, blank=True, null=True)
    reg_place_written_second_city = models.CharField(max_length=255, blank=True, null=True)
    physical_description = models.CharField(max_length=255, blank=True, null=True)
    # autograph_or_type = models.CharField(max_length=255, blank=True, null=True)
    # document_type = models.CharField(max_length=255, blank=True, null=True)
    # signed_or_initialed = models.CharField(max_length=255, blank=True, null=True)
    phys_descr_detail = models.CharField(max_length=255, blank=True, null=True)
    physDes_notes = models.CharField(max_length=255, blank=True, null=True)
    leaves  = models.CharField(max_length=255, blank=True, null=True)
    sides = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    postmark = models.CharField(max_length=255, blank=True, null=True)
    addressed_to_actual = models.CharField(max_length=255, blank=True, null=True)
    reg_recipient = models.CharField(max_length=255, blank=True, null=True)
    reg_place_sent = models.CharField(max_length=255, blank=True, null=True)
    reg_place_sent_city = models.CharField(max_length=255, blank=True, null=True)
    reg_place_sent_country = models.CharField(max_length=255, blank=True, null=True)
    additional = models.CharField(max_length=255, blank=True, null=True)
    repository = models.CharField(max_length=255, blank=True, null=True)
    public = models.CharField(max_length=255, blank=True, null=True)
    collection = models.CharField(max_length=255, blank=True, null=True)
    repository_information = models.CharField(max_length=255, blank=True, null=True)
    second_repository = models.CharField(max_length=255, blank=True, null=True)
    second_public = models.CharField(max_length=255, blank=True, null=True)
    owner_rights = models.CharField(max_length=255, blank=True, null=True)
    primary_language = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    sender = models.CharField(max_length=255, blank=True, null=True)
    place_prev_published = models.CharField(max_length=255, blank=True, null=True)
    verified = models.CharField(max_length=255, blank=True, null=True)



 
    'Linked Data Fields'
    repository_linked = models.ManyToManyField(Repository, blank=True, related_name='manyrespositories')
    recipients = models.ManyToManyField(Person, blank=True, related_name='manyrecipients')
    people = models.ManyToManyField(Person, blank=True, related_name='manypeople')
    places = models.ManyToManyField(Place, blank=True, related_name='manyplaces')
    organizations = models.ManyToManyField(Organization, blank=True, related_name='manyorganizations')
    productions = models.ManyToManyField(Production, blank=True, related_name='manyproductions')
    publications = models.ManyToManyField(Publication, blank=True, related_name='manypublications')
    directing = models.ManyToManyField(Directing, blank=True, related_name='manydirectings')
    writing = models.ManyToManyField(Writing, blank=True, related_name='manywritings')
    translating = models.ManyToManyField(Translating, blank=True, related_name='manytranslatings')
    reading = models.ManyToManyField(Reading, blank=True, related_name='manyreadings')
    attendance = models.ManyToManyField(Attendance, blank=True, related_name='manyattendances')
    public_events = models.ManyToManyField(Public_event, blank=True, related_name='manypublicevents')


    @property
    def month_to_string(self):
        month_dict = {
        0: '0',
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
    }
        return month_dict[self.month]




    
    def recipient_list(self):
        return "; ".join(['%s %s' % (r.first_name, r.last_name) for r in self.recipients.all()])

    def recipients_html(self):
        return format_html(self.recipients_excel)

    class Meta: 
        ordering = ['year', 'month', 'day']