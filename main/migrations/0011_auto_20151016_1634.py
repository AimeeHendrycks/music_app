# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20151016_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='album_information',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_bio',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='genre_title',
            field=models.TextField(null=True, blank=True),
        ),
    ]
