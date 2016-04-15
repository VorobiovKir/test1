# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0037_auto_20160302_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='agent',
            field=models.ForeignKey(blank=True, to='minimax.ExtinguishingAgent', null=True),
        ),
    ]
