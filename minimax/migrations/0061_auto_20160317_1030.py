# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import minimax.utils.model_utils
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0060_auto_20160317_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionMapPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_x', models.DecimalField(help_text=b'X Position (horizontal)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('position_y', models.DecimalField(help_text=b'Y Position (vertical)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('application_description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('application_description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('application_description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('application', models.ForeignKey(related_name='solution_map_points', to='minimax.Application')),
            ],
            options={
                'verbose_name': 'map point',
                'verbose_name_plural': 'map points',
            },
        ),
        migrations.AddField(
            model_name='solution',
            name='interactive_map_image',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='solutionmappoint',
            name='solution',
            field=models.ForeignKey(related_name='map_points', to='minimax.Solution'),
        ),
    ]
