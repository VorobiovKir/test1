# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0033_auto_20160301_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='slug',
        ),
    ]
