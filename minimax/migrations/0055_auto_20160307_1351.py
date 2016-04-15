# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0054_auto_20160307_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='secondary_description',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='secondary_description_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image', blank=True),
        ),
    ]
