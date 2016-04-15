# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0055_auto_20160307_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='secondary_description_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='secondary_description_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
    ]
