# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import django.core.validators
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0059_auto_20160308_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyFunctionTab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('teaser', models.TextField(default=b'', blank=True)),
                ('teaser_en', models.TextField(default=b'', null=True, blank=True)),
                ('teaser_de', models.TextField(default=b'', null=True, blank=True)),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('position', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'function tab',
                'verbose_name_plural': 'function tabs',
            },
        ),
        migrations.CreateModel(
            name='TechnologyMapPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('position_x', models.DecimalField(help_text=b'X Position (horizontal)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('position_y', models.DecimalField(help_text=b'Y Position (vertical)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'map point',
                'verbose_name_plural': 'map points',
            },
        ),
        migrations.RemoveField(
            model_name='application',
            name='description',
        ),
        migrations.RemoveField(
            model_name='application',
            name='description_de',
        ),
        migrations.RemoveField(
            model_name='application',
            name='description_en',
        ),
        migrations.AddField(
            model_name='technology',
            name='interactive_map_image',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='technologymappoint',
            name='technology',
            field=models.ForeignKey(related_name='map_points', to='minimax.Technology'),
        ),
        migrations.AddField(
            model_name='technologyfunctiontab',
            name='technology',
            field=models.ForeignKey(related_name='function_tabs', to='minimax.Technology'),
        ),
    ]
