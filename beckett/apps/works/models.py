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

    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Person)
    notes = models.TextField(blank=True)

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

