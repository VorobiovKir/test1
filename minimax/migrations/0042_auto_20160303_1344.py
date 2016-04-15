# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0041_auto_20160303_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='referenced_maps',
            field=models.ManyToManyField(related_name='technologies', to='minimax.InteractiveMap'),
        ),
    ]
