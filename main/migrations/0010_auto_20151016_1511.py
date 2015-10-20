# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151016_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='album_information',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
