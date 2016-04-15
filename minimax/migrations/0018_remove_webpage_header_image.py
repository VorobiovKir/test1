# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0017_auto_20160223_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='header_image',
        ),
    ]
