# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0068_auto_20160415_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='category',
            field=models.ForeignKey(related_name='category', default=1, to='minimax.NewsCategory'),
            preserve_default=False,
        ),
    ]
