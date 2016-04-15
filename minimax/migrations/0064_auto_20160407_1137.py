# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0063_auto_20160324_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_de',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='file_en',
            field=s3direct.fields.S3DirectField(null=True),
        ),
    ]
