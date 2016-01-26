# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160126_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ODNB_reference',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='VIAF_reference',
            field=models.URLField(null=True, blank=True),
        ),
    ]
