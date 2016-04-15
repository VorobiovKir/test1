# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0071_auto_20160415_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticleimage',
            name='article',
        ),
        migrations.DeleteModel(
            name='NewsArticleImage',
        ),
    ]
