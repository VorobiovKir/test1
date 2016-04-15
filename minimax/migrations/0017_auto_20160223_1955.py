# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0016_auto_20160223_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='header_caption',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
