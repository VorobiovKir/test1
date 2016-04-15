# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0052_auto_20160307_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='referenced_documents',
            field=models.ManyToManyField(related_name='solutions', verbose_name='documents', to='minimax.Document'),
        ),
    ]
