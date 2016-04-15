# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0069_newsarticle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='expire_on_homepage',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='show_on_homepage',
            field=models.BooleanField(default=True),
        ),
    ]
