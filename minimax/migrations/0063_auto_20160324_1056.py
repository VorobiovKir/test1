# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minimax', '0062_auto_20160317_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagetreeitem',
            name='menu_class',
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='title_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='title_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='title_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='certificationtype',
            name='title_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='name_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='name_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='quotation',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='quotation_de',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='quotation_en',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='responsibility',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='responsibility_de',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='responsibility_en',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extinguishingagent',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extinguishingagent',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extinguishingagent',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fair',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fair',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fair',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='interactive_map_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solutiontype',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solutiontype',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solutiontype',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='interactive_map_image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='referenced_applications',
            field=models.ManyToManyField(to='minimax.Application', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='referenced_certification_types',
            field=models.ManyToManyField(to='minimax.CertificationType', blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='referenced_technologies',
            field=models.ManyToManyField(to='minimax.Technology', blank=True),
        ),
        migrations.AlterField(
            model_name='technologyfunctiontab',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologyfunctiontab',
            name='title_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologyfunctiontab',
            name='title_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='image',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='title_de',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologymappoint',
            name='title_en',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologytype',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologytype',
            name='name_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='technologytype',
            name='name_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='title_de',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='title_en',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name_de',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name_en',
            field=models.CharField(help_text='The name of the page used in the navigation.', max_length=100, null=True, blank=True),
        ),
    ]
