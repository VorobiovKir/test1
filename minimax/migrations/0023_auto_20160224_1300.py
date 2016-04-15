# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0022_remove_webpage_body_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='header_caption_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='The caption of the banner.', null=True, verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_caption_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='The caption of the banner.', null=True, verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_title_de',
            field=models.CharField(help_text='The title text within the banner of the page.', max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='header_title_en',
            field=models.CharField(help_text='The title text within the banner of the page.', max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_caption',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='The caption of the banner.', verbose_name='caption', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_title',
            field=models.CharField(help_text='The title text within the banner of the page.', max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name_de',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name_en',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100, null=True),
        ),
    ]
