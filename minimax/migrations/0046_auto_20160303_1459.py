# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0045_auto_20160303_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
