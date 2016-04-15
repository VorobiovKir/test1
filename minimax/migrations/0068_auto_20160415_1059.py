# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0067_newscategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscategory',
            name='name_de',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='newscategory',
            name='name_en',
            field=models.CharField(max_length=126, null=True),
        ),
    ]
