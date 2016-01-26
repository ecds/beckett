# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160126_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventresource',
            name='Description',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
