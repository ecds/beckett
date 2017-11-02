from django.db import models
from tinymce import models as tinymce_models

from beckett.apps.people.models import Person

# Works
class ProductionManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Production(models.Model):
    '''Production of Beckett Work'''

    objects = ProductionManager()
    # django requires list of tuple for field choices
    profile_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    theatre = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']


class PublicationManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Publication(models.Model):

    objects = PublicationManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    translator = models.TextField(blank=True, null=True)
    place_pub_date = models.TextField(blank=True, null=True)
    #pages = models.CharField(max_length=255, blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class WritingManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Writing(models.Model):

    objects = WritingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class DirectingManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Directing(models.Model):

    objects = DirectingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']


class TranslatingManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Translating(models.Model):

    objects = TranslatingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    work = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    translator = models.TextField(blank=True, null=True)
    translated_title = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['work']

class ReadingManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Reading(models.Model):

    objects = ReadingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    author = models.TextField(blank=True, null=True)
    book = models.TextField(blank=True, null=True)
    publication = models.TextField(blank=True, null=True)

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['book']


