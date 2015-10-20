# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151016_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_location',
            field=models.TextField(null=True, blank=True),
        ),
    ]
