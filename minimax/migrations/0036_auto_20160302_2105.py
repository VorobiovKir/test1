# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0035_auto_20160302_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_de', models.CharField(max_length=200, null=True)),
                ('logo', s3direct.fields.S3DirectField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('thumbnail', s3direct.fields.S3DirectField()),
                ('file', models.FileField(upload_to=b'documents')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_de', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtinguishingAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characteristics', minimax.utils.model_utils.RichTextField(default=b'', blank=True)),
                ('characteristics_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('characteristics_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, blank=True)),
                ('agent', models.ForeignKey(to='minimax.ExtinguishingAgent', blank=True)),
                ('referenced_applications', models.ManyToManyField(to='minimax.Application')),
                ('referenced_solutions', models.ManyToManyField(to='minimax.Solution')),
                ('referenced_technologies', models.ManyToManyField(to='minimax.Technology')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(to='minimax.DocumentType', blank=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='referenced_applications',
            field=models.ManyToManyField(to='minimax.Application'),
        ),
    ]
