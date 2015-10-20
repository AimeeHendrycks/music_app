# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_albums_artists_tracks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_bio',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_images',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
