from django.db import models

from beckett.apps.people.models import Person

# Works
class WorkManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Work(models.Model):
    '''Publisher or other type of organization'''

    objects = WorkManager()
    # django requires list of tuple for field choices

    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Edition(models.Model):
    Year = models.IntegerField(blank=True, null=True)
    ISBN = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    publisher_or_producer = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    work = models.ForeignKey(Work, blank=True, null=True)