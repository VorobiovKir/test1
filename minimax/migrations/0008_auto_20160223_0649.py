# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0007_auto_20160217_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetreeitem',
            name='teaser',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='pagetreeitem',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
