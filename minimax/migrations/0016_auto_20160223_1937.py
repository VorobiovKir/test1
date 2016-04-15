# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0015_pagecontent_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecontent',
            options={'ordering': ['position'], 'verbose_name': 'page content', 'verbose_name_plural': 'page content'},
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Position', blank=True),
        ),
    ]
