# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20160126_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='location',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='edition',
            name='publisher_or_producer',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
