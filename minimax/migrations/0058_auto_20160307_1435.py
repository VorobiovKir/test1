# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0057_auto_20160307_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser',
            field=models.TextField(default=b'', null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser_de',
            field=models.TextField(default=b'', null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser_en',
            field=models.TextField(default=b'', null=True, verbose_name='teaser', blank=True),
        ),
    ]
