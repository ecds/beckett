# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=100, null=True, blank=True)),
                ('Year', models.IntegerField(null=True, blank=True)),
                ('language', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
