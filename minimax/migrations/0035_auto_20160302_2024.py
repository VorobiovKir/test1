# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('minimax', '0034_remove_webpage_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractiveMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('teaser', models.CharField(default=b'', max_length=255, blank=True)),
                ('teaser_en', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('teaser_de', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('position_x', models.PositiveIntegerField(help_text=b'X Position (horizontal)')),
                ('position_y', models.PositiveIntegerField(help_text=b'Y Position (vertical)')),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('interactive_map', models.ForeignKey(related_name='map_points', to='minimax.InteractiveMap')),
            ],
        ),
        migrations.AddField(
            model_name='technology',
            name='applications_teaser',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='applications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='applications_teaser_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='applications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='applications_teaser_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='applications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='certifications_teaser',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='certifications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='certifications_teaser_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='certifications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='certifications_teaser_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='certifications', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_1',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_1_de',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_1_en',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_2',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_2_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='header_text_2_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='primary_description',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='primary description', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='primary_description_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='primary description', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='primary_description_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='primary description', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='primary_description_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='technologies_teaser',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='technologies', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='technologies_teaser_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='technologies', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='technologies_teaser_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='technologies', blank=True),
        ),
    ]
