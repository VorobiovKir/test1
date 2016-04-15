# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0011_webpage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
    ]
