# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0010_auto_20160223_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(unique=True, null=True, verbose_name=models.CharField(max_length=100)),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.ForeignKey(to='minimax.ServiceType'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='type',
            field=models.ForeignKey(to='minimax.SolutionType'),
        ),
    ]
