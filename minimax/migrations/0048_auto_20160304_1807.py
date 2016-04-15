# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0047_auto_20160304_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file_de',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file_en',
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.FileField(default=None, max_length=150, upload_to=b'documents'),
            preserve_default=False,
        ),
    ]
