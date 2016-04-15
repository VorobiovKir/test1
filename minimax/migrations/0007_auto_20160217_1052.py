# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0006_auto_20160217_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecontent',
            old_name='description',
            new_name='text',
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='image_caption_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='image_caption_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='text_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='text_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='title_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='title_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
