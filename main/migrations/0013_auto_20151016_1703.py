# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151016_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_related_projects',
            field=models.TextField(null=True, blank=True),
        ),
    ]
