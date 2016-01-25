# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address', models.CharField(help_text=b'Street name and number', max_length=255, blank=True)),
                ('city', models.CharField(help_text=b'City name', max_length=255)),
                ('state', models.CharField(help_text=b'State name', max_length=255, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=10, blank=True)),
                ('country', models.CharField(help_text=b'Country name', max_length=255)),
                ('Latitude', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
                ('Longitude', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
            ],
        ),
    ]
