# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0008_auto_20160223_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetreeitem',
            name='teaser_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='pagetreeitem',
            name='teaser_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='pagetreeitem',
            name='title_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagetreeitem',
            name='title_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
