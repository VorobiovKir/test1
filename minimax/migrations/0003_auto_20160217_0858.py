# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc

import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0002_newsarticle_key_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', s3direct.fields.S3DirectField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['-publication_date'], 'verbose_name': 'news article', 'verbose_name_plural': 'news articles'},
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 8, 58, 55, 43841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='key_image',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='newsarticleimage',
            name='article',
            field=models.ForeignKey(to='minimax.NewsArticle'),
        ),
    ]
