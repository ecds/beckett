from django.db import models

from beckett.apps.people.models import Person

# Worksff
class ProductionManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Production(models.Model):
    '''Production of Beckett Work'''

    objects = ProductionManager()
    # django requires list of tuple for field choices
    profile_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
    directors = models.ManyToManyField(Person, related_name="Production_directors", blank=True)
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
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
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
    '''Publisher or other type of organization'''

    objects = WritingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
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
    '''Publisher or other type of organization'''

    objects = DirectingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
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
    '''Publisher or other type of organization'''

    objects = TranslatingManager()
    # django requires list of tuple for field choices

    profile_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Person, blank=True)
    notes = models.TextField(blank=True, null=True, verbose_name = "Description or Notes")

    def natural_key(self):
        return (self.title,)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

