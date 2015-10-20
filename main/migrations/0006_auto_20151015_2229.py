# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151015_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_bio',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
