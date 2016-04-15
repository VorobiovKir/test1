# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0009_auto_20160223_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='image_position',
            field=models.CharField(default=b'LEFT', choices=[(b'LEFT', 'Left'), (b'RIGHT', 'Right')], max_length=15, blank=True, null=True, verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='image_width',
            field=models.PositiveSmallIntegerField(default=33, null=True, verbose_name='width', blank=True, choices=[(25, b'25%'), (33, b'33%'), (50, b'50%')]),
        ),
    ]
