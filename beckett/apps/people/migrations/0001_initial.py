# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PenName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uri', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name_plural': 'People',
            },
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('first_name', 'last_name')]),
        ),
        migrations.AddField(
            model_name='penname',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
        migrations.AddField(
            model_name='name',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
    ]
