# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151016_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_members',
            field=models.TextField(null=True, blank=True),
        ),
    ]
