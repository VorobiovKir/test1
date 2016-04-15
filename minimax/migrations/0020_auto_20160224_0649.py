# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0019_auto_20160223_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetreeitem',
            name='menu_class',
            field=models.CharField(help_text=b'Class to be added to the menu tag', max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagetreeitem',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
    ]
