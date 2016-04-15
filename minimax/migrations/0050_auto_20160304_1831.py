# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0049_auto_20160304_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.FileField(max_length=150, null=True, upload_to=b'documents', blank=True),
        ),
    ]
