# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'fair',
                'verbose_name_plural': 'fairs',
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_de', models.CharField(max_length=100, null=True)),
                ('teaser', models.TextField(null=True, verbose_name='teaser', blank=True)),
                ('teaser_en', models.TextField(null=True, verbose_name='teaser', blank=True)),
                ('teaser_de', models.TextField(null=True, verbose_name='teaser', blank=True)),
                ('description', minimax.utils.model_utils.RichTextField(default=b'', verbose_name='description', blank=True)),
                ('description_en', minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
                ('description_de', minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'news article',
                'verbose_name_plural': 'news articles',
            },
        ),
        migrations.CreateModel(
            name='PageTreeItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('position', models.PositiveIntegerField()),
                ('type', models.CharField(default=b'STANDARD', max_length=15, verbose_name='type', choices=[(b'STANDARD', 'Standard'), (b'MENU_ITEM', 'Menu item'), (b'HOME', 'Home'), (b'TECHNOLOGIES', 'Technologies'), (b'SOLUTIONS', 'Solutions'), (b'SERVICES', 'Services')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='minimax.PageTreeItem', null=True)),
            ],
            options={
                'verbose_name': 'Navigation entry',
                'verbose_name_plural': 'Navigation entries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
                ('default_language', models.CharField(default=(b'en', b'English'), max_length=15, choices=[(b'en', b'English'), (b'de', b'German')])),
                ('active', models.PositiveIntegerField(default=0, choices=[(1, 'Yes'), (0, 'No')])),
                ('active_en', models.PositiveIntegerField(default=0, null=True, choices=[(1, 'Yes'), (0, 'No')])),
                ('active_de', models.PositiveIntegerField(default=0, null=True, choices=[(1, 'Yes'), (0, 'No')])),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'service type',
                'verbose_name_plural': 'service types',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'solution',
                'verbose_name_plural': 'solutions',
            },
        ),
        migrations.CreateModel(
            name='SolutionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'solution type',
                'verbose_name_plural': 'solution types',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'technology',
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='TechnologyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'technology type',
                'verbose_name_plural': 'technology types',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'training',
                'verbose_name_plural': 'trainings',
            },
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_en', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('status_de', models.CharField(default=b'HIDDEN', max_length=15, null=True, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')])),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_de', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'web page',
                'verbose_name_plural': 'web pages',
            },
        ),
        migrations.CreateModel(
            name='WebPageRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_tree_item', models.ForeignKey(related_name='pages', to='minimax.PageTreeItem')),
                ('region', models.ForeignKey(to='minimax.Region')),
                ('web_page', models.ForeignKey(related_name='related_page_tree_items', to='minimax.WebPage')),
            ],
            options={
                'ordering': ['region__id'],
                'verbose_name': 'related web page',
                'verbose_name_plural': 'related web pages',
            },
        ),
        migrations.AddField(
            model_name='technology',
            name='type',
            field=models.ForeignKey(to='minimax.TechnologyType'),
        ),
        migrations.AddField(
            model_name='solution',
            name='type',
            field=models.ForeignKey(to='minimax.TechnologyType'),
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(to='minimax.TechnologyType'),
        ),
        migrations.AlterUniqueTogether(
            name='webpagerelation',
            unique_together=set([('region', 'page_tree_item')]),
        ),
    ]
