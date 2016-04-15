# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0030_auto_20160301_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='type',
            field=models.ForeignKey(related_name='solutions', to='minimax.SolutionType'),
        ),
    ]
