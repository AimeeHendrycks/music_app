# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_id', models.IntegerField(null=True, blank=True)),
                ('artist_handle', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_url', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_name', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_bio', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_members', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_website', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_wikipedia_page', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_donation_url', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_contact', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_location', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_active_year_begin', models.IntegerField(null=True, blank=True)),
                ('artist_active_year_end', models.IntegerField(null=True, blank=True)),
                ('artist_related_projects', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_associated_labels', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_comments', models.IntegerField(null=True, blank=True)),
                ('artist_favorites', models.IntegerField(null=True, blank=True)),
                ('artist_date_created', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_flattr_name', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_paypal_name', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_latitude', models.FloatField(null=True, blank=True)),
                ('artist_longitude', models.FloatField(null=True, blank=True)),
                ('artist_image_file', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_images', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
