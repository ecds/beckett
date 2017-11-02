from django.db import models
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person

class Chronology(models.Model):
    'Events in the published chronologies'

    objects = models.Manager()

    sequence = models.DecimalField(null=True, max_digits=7, decimal_places=3)
    year = models.IntegerField(null=True)
    label = models.CharField(max_length=255, null=True, verbose_name="Date range")
    description = tinymce_models.HTMLField(null=True)
    # add date fields

    class Meta:
        verbose_name_plural = 'Published Chronologies'
        ordering = ['sequence']

class EventResource(models.Model):

    Type = models.CharField(max_length=500, blank=True, null=True)
    Description = models.CharField(max_length=500, blank=True, null=True)
    URL_Content = models.URLField(max_length=1000, blank=True, null=True, verbose_name="URL or other resource content")
    Permissions = models.CharField(max_length=500, blank=True, null=True)
    Date_Accessed = models.CharField(max_length=255, blank=True, null=True)
    Chronology_Item = models.ForeignKey(Chronology)

class AttendanceManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Attendance(models.Model):

    objects = AttendanceManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    thing = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    place_date = models.CharField(max_length=255, blank=True, null=True)
    attends_with = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['thing']

class Public_eventManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Public_event(models.Model):

    objects = Public_eventManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.event,)

    def __unicode__(self):
        return self.event

    class Meta:
        ordering = ['event']