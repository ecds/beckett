# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_edition_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='notes',
            field=models.TextField(verbose_name=b'Description or Notes', blank=True),
        ),
    ]
