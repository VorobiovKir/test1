# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0066_auto_20160408_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=126)),
                ('color', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
            },
        ),
    ]
