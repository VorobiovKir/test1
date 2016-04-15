# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0026_auto_20160224_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default=b'HIDDEN', max_length=15, verbose_name='status', choices=[(b'HIDDEN', 'Hidden'), (b'PUBLISHED', 'Published')]),
        ),
    ]
