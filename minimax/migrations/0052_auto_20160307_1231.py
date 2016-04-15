# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0051_technology_referenced_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='header_text_1',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='header_text_2',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='primary_description',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='primary_description_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='referenced_documents',
            field=models.ManyToManyField(to='minimax.Document', verbose_name='documents'),
        ),
        migrations.AddField(
            model_name='solution',
            name='referenced_maps',
            field=models.ManyToManyField(related_name='solutions', to='minimax.InteractiveMap'),
        ),
    ]
