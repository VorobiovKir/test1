# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0014_auto_20160223_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Position'),
        ),
    ]
