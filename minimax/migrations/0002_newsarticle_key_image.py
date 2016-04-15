# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='key_image',
            field=models.ImageField(null=True, upload_to=b'test', blank=True),
        ),
    ]
