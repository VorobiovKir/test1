# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import s3direct


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0004_auto_20160217_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'TEXT', max_length=15, verbose_name='type', choices=[(b'TEXT', 'Text'), (b'TEXT_W_IMAGE', 'Text with image'), (b'TEXT_W_BGIMAGE', 'Text with background image')])),
                ('title', models.CharField(max_length=255)),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', verbose_name='text', blank=True)),
                ('image', s3direct.fields.S3DirectField(null=True)),
                ('image_position', models.CharField(default=b'LEFT', max_length=15, verbose_name='position', choices=[(b'LEFT', 'Left'), (b'RIGHT', 'Right')])),
                ('image_width', models.PositiveSmallIntegerField(default=b'33', verbose_name='width', choices=[(b'25', b'25%'), (b'33', b'33%'), (b'50', b'50%')])),
                ('image_caption', models.CharField(max_length=255)),
                ('page', models.ForeignKey(related_name='content', to='minimax.WebPage')),
            ],
            options={
                'verbose_name': 'page content',
                'verbose_name_plural': 'page content',
            },
        ),
        migrations.AlterModelOptions(
            name='newsarticleimage',
            options={'ordering': ['position'], 'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterField(
            model_name='pagetreeitem',
            name='type',
            field=models.CharField(default=b'STANDARD', max_length=15, verbose_name='type', choices=[(b'STANDARD', 'Standard'), (b'MENU_ITEM', 'Menu item'), (b'HOME', 'Home'), (b'NEWS', 'News'), (b'FAIRS', 'Fairs'), (b'TRAININGS', 'Trainings'), (b'PEOPLE', 'People'), (b'TECHNOLOGIES', 'Technologies'), (b'SOLUTIONS', 'Solutions'), (b'SERVICES', 'Services'), (b'DOWNLOADS', 'Downloads'), (b'CONTACT', 'Contact')]),
        ),
    ]
