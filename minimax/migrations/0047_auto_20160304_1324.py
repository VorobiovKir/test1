# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0046_auto_20160303_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='related_services',
            field=models.ManyToManyField(related_name='customers', to='minimax.Service', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_solutions',
            field=models.ManyToManyField(related_name='customers', to='minimax.Solution', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_technologies',
            field=models.ManyToManyField(related_name='customers', to='minimax.Technology', blank=True),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='position_x',
            field=models.DecimalField(help_text=b'X Position (horizontal)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='position_y',
            field=models.DecimalField(help_text=b'Y Position (vertical)', max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_applications',
            field=models.ManyToManyField(related_name='projects', to='minimax.Application', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_solutions',
            field=models.ManyToManyField(related_name='projects', to='minimax.Solution', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='referenced_technologies',
            field=models.ManyToManyField(related_name='projects', to='minimax.Technology', blank=True),
        ),
    ]
