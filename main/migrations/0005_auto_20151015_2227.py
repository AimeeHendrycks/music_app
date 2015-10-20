# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151015_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_bio',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
