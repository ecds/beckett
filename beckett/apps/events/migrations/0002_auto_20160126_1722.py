# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(max_length=500, null=True, blank=True)),
                ('URL_Content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='chronology',
            name='label',
            field=models.CharField(max_length=255, verbose_name=b'Date range'),
        ),
        migrations.AddField(
            model_name='eventresource',
            name='Chronology_Item',
            field=models.ForeignKey(to='events.Chronology'),
        ),
    ]
