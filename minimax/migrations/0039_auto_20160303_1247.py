# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0038_auto_20160302_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interactivemap',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='interactivemap',
            name='object_id',
        ),
        migrations.AddField(
            model_name='technology',
            name='referenced_maps',
            field=models.ManyToManyField(related_name='technologies', null=True, to='minimax.InteractiveMap', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_applications',
            field=models.ManyToManyField(related_name='projects', to='minimax.Application'),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_solutions',
            field=models.ManyToManyField(related_name='projects', to='minimax.Solution'),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_technologies',
            field=models.ManyToManyField(related_name='projects', to='minimax.Technology'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_1',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_1_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_1_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_2',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_2_de',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_text_2_en',
            field=models.TextField(null=True, verbose_name='text', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='primary_description',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='primary_description_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='primary_description_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='primary_description_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image', blank=True),
        ),
    ]
