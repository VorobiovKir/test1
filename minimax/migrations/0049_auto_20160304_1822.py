# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0048_auto_20160304_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.ForeignKey(blank=True, to='minimax.DocumentType', null=True),
        ),
    ]
