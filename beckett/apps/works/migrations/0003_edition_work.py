# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='work',
            field=models.ForeignKey(blank=True, to='works.Work', null=True),
        ),
    ]
