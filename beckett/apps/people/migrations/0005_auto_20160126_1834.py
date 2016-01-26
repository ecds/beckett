# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160126_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ODNB_reference',
            field=models.CharField(help_text=b'ODNB reference citation including permalink', max_length=500, null=True, blank=True),
        ),
    ]
