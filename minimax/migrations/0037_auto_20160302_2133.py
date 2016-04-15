# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0036_auto_20160302_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='referenced_certification_types',
            field=models.ManyToManyField(to='minimax.CertificationType'),
        ),
        migrations.AddField(
            model_name='technology',
            name='referenced_customers',
            field=models.ManyToManyField(to='minimax.Customer'),
        ),
        migrations.AddField(
            model_name='technology',
            name='referenced_technologies',
            field=models.ManyToManyField(to='minimax.Technology'),
        ),
    ]
