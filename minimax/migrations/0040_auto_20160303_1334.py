# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0039_auto_20160303_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='referenced_customers',
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='customer',
            name='related_service',
            field=models.ManyToManyField(related_name='customers', to='minimax.Service'),
        ),
        migrations.AddField(
            model_name='customer',
            name='related_solution',
            field=models.ManyToManyField(related_name='customers', to='minimax.Solution'),
        ),
        migrations.AddField(
            model_name='customer',
            name='related_technologies',
            field=models.ManyToManyField(related_name='customers', to='minimax.Technology'),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='description_de',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='teaser_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='characteristics',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='characteristics_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='characteristics_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
