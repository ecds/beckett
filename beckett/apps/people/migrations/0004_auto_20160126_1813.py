# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160126_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=500, null=True, blank=True)),
                ('Link', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='ODNB_reference',
            field=models.CharField(help_text=b'ODNB Reference Number', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='VIAF_reference',
            field=models.URLField(help_text=b'VIAF Permalink', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personresource',
            name='person',
            field=models.ForeignKey(related_name='resources', blank=True, to='people.Person', null=True),
        ),
    ]
