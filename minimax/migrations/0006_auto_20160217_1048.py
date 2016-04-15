# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0005_auto_20160217_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='image_caption',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='image_width',
            field=models.PositiveSmallIntegerField(default=33, verbose_name='width', choices=[(25, b'25%'), (33, b'33%'), (50, b'50%')]),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
