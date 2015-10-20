# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151015_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='album_comments',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_date_created',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_date_released',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_engineer',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_favorites',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_handle',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_image_file',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_information',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_listens',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_producer',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_tracks',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_type',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='album_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='artist_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='albums',
            name='artist_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='album_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='album_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='album_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='artist_id',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='artist_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='artist_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='artist_website',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='license_image_file',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='license_image_file_large',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='license_parent_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='license_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='license_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_bit_rate',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_comments',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_composer',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_copyright_c',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_copyright_p',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_date_created',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_date_recorded',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_disc_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_duration',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_explicit',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_explicit_notes',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_favorites',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_file',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_id',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_image_file',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_information',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_instrumental',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_interest',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_language_code',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_listens',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_lyricist',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_publisher',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_donation_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_website',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='artist_wikipedia_page',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]
