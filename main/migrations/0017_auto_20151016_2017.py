# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20151016_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='artist_url',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='artist_id',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='artist_url',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='artist_website',
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(blank=True, to='main.Artists', null=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='artist',
            field=models.ForeignKey(blank=True, to='main.Artists', null=True),
        ),
    ]
