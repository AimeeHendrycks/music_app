# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151015_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artists',
            name='artist_images',
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_bio',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
