from django.db import models

# Organizations
class OrganizationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Organization(models.Model):
    '''Publisher or other type of organizaiton'''

    objects = OrganizationManager()
    # django requires list of tuple for field choices

    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def natural_key(self):
        return (self.name,)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Person and person parts
class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


class Person(models.Model):
    'A person associated with a letter, work, etc.'

    objects = PersonManager()

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    uri = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def natural_key(self):
        return (self.first_name, self.last_name)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = u'People'
        unique_together = ('first_name', 'last_name')
        ordering = ['last_name', 'first_name']



class NameManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name, person):
        self.get(first_name=first_name, last_name=last_name)


class Name(models.Model):
    # alternate name
    # For people like LeRoi Jones / Amiri Baraka where the person
    # actually has different names during their life.
    # It would also cover maiden / married names.

    objects = NameManager()

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    person = models.ForeignKey('Person')

    def natural_key(self):
        return (self.first_name, self.last_name)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class PenNameManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class PenName(models.Model):
    # Pen names are for someone like Mark Twain, who used a pen name
    # for publication his whole life but didn't go by it in person.

    objects = PenNameManager()

    name = models.CharField(max_length=200)
    person = models.ForeignKey('Person')

    def natural_key(self):
        return (self.name)

    def __unicode__(self):
        return self.name