# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0031_auto_20160301_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='solutiontype',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
    ]
