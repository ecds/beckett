# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160126_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventresource',
            name='Date_Accessed',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='eventresource',
            name='Permissions',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eventresource',
            name='URL_Content',
            field=models.URLField(max_length=1000, null=True, verbose_name=b'URL or other resource content', blank=True),
        ),
    ]
