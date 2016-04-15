# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0003_auto_20160217_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticleimage',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
