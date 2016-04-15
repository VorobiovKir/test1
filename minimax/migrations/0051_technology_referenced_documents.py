# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0050_auto_20160304_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='referenced_documents',
            field=models.ManyToManyField(to='minimax.Document', verbose_name='documents'),
        ),
    ]
