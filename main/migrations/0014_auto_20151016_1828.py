# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151016_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_information',
            field=models.TextField(null=True, blank=True),
        ),
    ]
