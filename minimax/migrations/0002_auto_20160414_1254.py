# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='interactive_map_image_de',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='interactive_map_image_en',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
