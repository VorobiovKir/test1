# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0040_auto_20160303_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name_en',
        ),
        migrations.AddField(
            model_name='application',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='application',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='document',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='document',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='interactivemap',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='project',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='project',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
    ]
