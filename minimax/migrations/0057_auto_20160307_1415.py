# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import minimax.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0056_auto_20160307_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='secondary_description_image',
            new_name='technologies_image',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='secondary_description',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='secondary_description_de',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='secondary_description_en',
        ),
        migrations.AddField(
            model_name='solution',
            name='referenced_technologies',
            field=models.ManyToManyField(to='minimax.Technology', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='technologies_teaser',
            field=minimax.utils.model_utils.RichTextField(default=b'', verbose_name='technologies', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='technologies_teaser_de',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='technologies', blank=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='technologies_teaser_en',
            field=minimax.utils.model_utils.RichTextField(default=b'', null=True, verbose_name='technologies', blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='referenced_documents',
            field=models.ManyToManyField(related_name='solutions', verbose_name='documents', to='minimax.Document', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='referenced_documents',
            field=models.ManyToManyField(to='minimax.Document', verbose_name='documents', blank=True),
        ),
    ]
