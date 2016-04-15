# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0053_auto_20160307_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='header_text_1_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='header_text_1_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='header_text_2_de',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='header_text_2_en',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='primary_description_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='primary_description_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
    ]
