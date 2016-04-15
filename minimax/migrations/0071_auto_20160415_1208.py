# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0070_auto_20160415_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='teaser',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='teaser_de',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='teaser_en',
        ),
    ]
