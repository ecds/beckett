from django.db import models
from tinymce import models as tinymce_models


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