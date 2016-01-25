from django.db import models
from tinymce import models as tinymce_models


class Chronology(models.Model):
    'Events in the published chronologies'

    objects = models.Manager()

    sequence = models.DecimalField(max_digits=7, decimal_places=3)
    year = models.IntegerField()
    label = models.CharField(max_length=255)
    description = tinymce_models.HTMLField()
    # add date fields

    class Meta:
        verbose_name_plural = 'Published Chronologies'
        ordering = ['sequence']
        