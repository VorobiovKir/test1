# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0024_auto_20160224_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecontent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='title_en',
        ),
    ]
