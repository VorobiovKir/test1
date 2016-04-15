# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0028_auto_20160224_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name_en',
        ),
    ]
