# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0061_auto_20160317_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mappoint',
            name='interactive_map',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='referenced_maps',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='referenced_maps',
        ),
        migrations.DeleteModel(
            name='InteractiveMap',
        ),
        migrations.DeleteModel(
            name='MapPoint',
        ),
    ]
