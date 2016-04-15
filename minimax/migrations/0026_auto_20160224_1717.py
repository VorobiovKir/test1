# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0025_auto_20160224_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('responsibility', models.CharField(max_length=50)),
                ('quotation', models.CharField(max_length=255)),
                ('text', minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True)),
                ('image', s3direct.fields.S3DirectField(null=True)),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.AlterModelOptions(
            name='pagecontent',
            options={'ordering': ['position'], 'verbose_name': 'content element', 'verbose_name_plural': 'content section'},
        ),
        migrations.AlterField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(help_text='URL segment .../page-name/... in browser', max_length=100, unique=True, null=True),
        ),
    ]
