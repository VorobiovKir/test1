# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0043_auto_20160303_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='related_service',
            new_name='related_services',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='related_solution',
            new_name='related_solutions',
        )
    ]
