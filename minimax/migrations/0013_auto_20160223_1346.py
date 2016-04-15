# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0012_auto_20160223_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(help_text=b'Full path without leading slash.', max_length=255)),
            ],
            options={
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
        ),
        migrations.AddField(
            model_name='webpage',
            name='body_class',
            field=models.CharField(help_text=b'Class to be added to the body tag', max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='template',
            field=models.ForeignKey(related_name='pages', to='minimax.Template', null=True),
        ),
    ]
