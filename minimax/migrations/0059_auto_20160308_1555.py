# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0058_auto_20160307_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_left',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description left column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description left column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description left column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image left column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_image_title',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_image_title_de',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_left_image_title_en',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='if left blank, the description will be rendered on one column', verbose_name='description right column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='if left blank, the description will be rendered on one column', null=True, verbose_name='description right column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', help_text='if left blank, the description will be rendered on one column', null=True, verbose_name='description right column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image right column', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_image_title',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_image_title_de',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_right_image_title_en',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_title_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_title_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='details_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='details image', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='details_text',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='scope in details', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='details_text_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='scope in details', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='details_text_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='scope in details', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_1',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_1_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_1_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_2',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_2_de',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='header_text_2_en',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
    ]
