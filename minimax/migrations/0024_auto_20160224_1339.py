# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0023_auto_20160224_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser_de',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='pagetreeitem',
            name='teaser_en',
            field=models.TextField(null=True, verbose_name='teaser', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_caption',
            field=models.TextField(default=b'', verbose_name='caption', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_caption_de',
            field=models.TextField(default=b'', null=True, verbose_name='caption', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_caption_en',
            field=models.TextField(default=b'', null=True, verbose_name='caption', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_title',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
    ]
