# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0021_auto_20160224_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='body_class',
        ),
    ]
