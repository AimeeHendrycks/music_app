# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151016_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_file',
            field=models.TextField(null=True, blank=True),
        ),
    ]
