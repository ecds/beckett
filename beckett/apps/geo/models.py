from django.db import models


class PlaceManager(models.Manager):
    def get_by_natural_key(self, street_address, city, zipcode):
        return self.get(street_address=street_address, city=city, zipcode=zipcode)


class Place(models.Model):
    """
    Locations or Addresses
    """

    objects = PlaceManager()

    #: Street name and number
    street_address = models.CharField(max_length=255, blank=True, null=True, help_text='Street name and number')
    #: City name
    city = models.CharField(max_length=255, null=True, help_text='City name')
    #: state - :class:`StateCode`
    state = models.CharField(max_length=255, blank=True, null=True, help_text='State name')
    #: zipcode
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    #: country - :class:`GeonamesCountry`
    country = models.CharField(max_length=255, blank=True, null=True, help_text='Country name')

    Latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)

    # generate natural key
    def natural_key(self):
        return (self.street_address, self.city, self.zipcode)

    def __unicode__(self):
        # only include fields that are not empty
        fields = [self.street_address, self.city, self.state, self.zipcode, self.country]
        return ' '.join([unicode(f) for f in fields if f])
        

class Repository(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, help_text='Collection name or Descriptive name')
    abb = models.CharField(max_length=255, blank=True, null=True)
    descriptive_information = models.CharField(max_length=500, blank=True, null=True, help_text='Additional collection data or Foundation name')
    storage_information = models.CharField(max_length=255, blank=True, null=True, help_text='Box number or ID number')


    #: Street name and number
    street_address = models.CharField(max_length=255, blank=True, null=True, help_text='Street name and number')
    #: City name
    city = models.CharField(max_length=255, blank=True, null=True, help_text='City name')
    #: state - :class:`StateCode`
    state = models.CharField(max_length=255, blank=True, null=True, help_text='State name')
    #: zipcode
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    #: country - :class:`GeonamesCountry`
    country = models.CharField(max_length=255, blank=True, null=True, help_text='Country name')

    Latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)

    URL = models.CharField(max_length=255, blank=True, null=True, help_text='Finding Aid Link')

    def __unicode__(self):
        # only include fields that are not empty
        fields = [self.name, self.descriptive_information, self.street_address, self.city, self.state, self.zipcode, self.country]
        return ' '.join([unicode(f) for f in fields if f])
    class Meta:
        verbose_name_plural = 'Repositories'
