# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0018_remove_webpage_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='header_title',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
    ]
