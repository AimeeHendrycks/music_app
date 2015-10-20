# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151015_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='album_information',
            field=models.CharField(max_length=750, null=True, blank=True),
        ),
    ]
