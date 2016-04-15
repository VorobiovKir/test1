# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0065_auto_20160408_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='referenced_documents',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='referenced_documents',
        ),
        migrations.AddField(
            model_name='document',
            name='related_solution_types',
            field=models.ManyToManyField(related_name='documents', to='minimax.SolutionType', blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='related_solutions',
            field=models.ManyToManyField(related_name='documents', to='minimax.Solution', blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='related_technologies',
            field=models.ManyToManyField(related_name='documents', to='minimax.Technology', blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='related_technology_types',
            field=models.ManyToManyField(related_name='documents', to='minimax.TechnologyType', blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='solution_relation_type',
            field=models.CharField(default=b'I', max_length=15, verbose_name='Type', choices=[(b'A', 'All'), (b'T', 'By type'), (b'I', 'By item')]),
        ),
        migrations.AddField(
            model_name='document',
            name='technology_relation_type',
            field=models.CharField(default=b'I', max_length=15, verbose_name='Type', choices=[(b'A', 'All'), (b'T', 'By type'), (b'I', 'By item')]),
        ),
    ]
