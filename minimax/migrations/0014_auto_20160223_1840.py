# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0013_auto_20160223_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='template',
            field=models.ForeignKey(related_name='pages', blank=True, to='minimax.Template', null=True),
        ),
    ]
