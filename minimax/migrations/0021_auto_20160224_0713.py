# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0020_auto_20160224_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser',
            field=minimax.utils.model_utils.RichTextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser_de',
            field=minimax.utils.model_utils.RichTextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser_en',
            field=minimax.utils.model_utils.RichTextField(null=True, verbose_name='teaser', blank=True),
        ),
    ]
