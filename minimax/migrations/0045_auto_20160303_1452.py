# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0044_auto_20160303_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AlterField(
            model_name='interactivemap',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='key_image',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AlterField(
            model_name='newsarticleimage',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='primary_description_image',
            field=s3direct.fields.S3DirectField(null=True, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='header_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
