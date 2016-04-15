# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0029_auto_20160224_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name': 'technology', 'verbose_name_plural': 'technologies'},
        ),
        migrations.AddField(
            model_name='technology',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='technologytype',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='type',
            field=models.ForeignKey(related_name='technologies', to='minimax.TechnologyType'),
        ),
    ]
