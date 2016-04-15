# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0027_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='quotation_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='quotation_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='responsibility_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='responsibility_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='status_de',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='employee',
            name='status_en',
            field=models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
        migrations.AddField(
            model_name='employee',
            name='text_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='text_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True),
        ),
    ]
