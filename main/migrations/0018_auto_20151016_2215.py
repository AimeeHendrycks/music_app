# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151016_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracks',
            name='album_id',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='album_title',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='album_url',
        ),
        migrations.AddField(
            model_name='tracks',
            name='album',
            field=models.ForeignKey(blank=True, to='main.Albums', null=True),
        ),
    ]
