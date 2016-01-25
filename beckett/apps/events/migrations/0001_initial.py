# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chronology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.DecimalField(max_digits=7, decimal_places=3)),
                ('year', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
                'ordering': ['sequence'],
                'verbose_name_plural': 'Published Chronologies',
            },
        ),
    ]
