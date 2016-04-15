# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0032_auto_20160301_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['name'], 'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'ordering': ['name'], 'verbose_name': 'solution', 'verbose_name_plural': 'solutions'},
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.ForeignKey(related_name='services', to='minimax.ServiceType'),
        ),
    ]
