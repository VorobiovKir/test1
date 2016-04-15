# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0042_auto_20160303_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_de',
            field=models.FileField(null=True, upload_to=b'documents'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_en',
            field=models.FileField(null=True, upload_to=b'documents'),
        ),
    ]
