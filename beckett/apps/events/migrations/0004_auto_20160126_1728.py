# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160126_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventresource',
            name='Date_Accessed',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
