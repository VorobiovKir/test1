# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0064_auto_20160407_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.ForeignKey(default=1, to='minimax.DocumentType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solutionmappoint',
            name='position_x',
            field=models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='solutionmappoint',
            name='position_y',
            field=models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='position_x',
            field=models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='position_y',
            field=models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
