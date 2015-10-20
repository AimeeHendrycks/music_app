from django.db import models

# Create your models here.

class Genres(models.Model):
    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title =  models.TextField(null=True, blank=True)
    genre_handle = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.genre_title

class Artists(models.Model):
    artist_id = models.IntegerField(null=True, blank=True)
    artist_handle = models.CharField(max_length=255, null=True, blank=True)
    artist_url = models.URLField(max_length=255, null=True, blank=True)
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    artist_bio = models.TextField(null=True, blank=True)
    artist_members = models.TextField(null=True, blank=True)
    artist_website = models.URLField(max_length=255, null=True, blank=True)
    artist_wikipedia_page = models.URLField(max_length=255, null=True, blank=True)
    artist_donation_url = models.URLField(max_length=255, null=True, blank=True)
    artist_contact = models.CharField(max_length=255, null=True, blank=True)
    artist_location = models.TextField(null=True, blank=True)
    artist_active_year_begin = models.IntegerField(null=True, blank=True)
    artist_active_year_end = models.IntegerField(null=True, blank=True)
    artist_related_projects = models.TextField(null=True, blank=True)
    artist_associated_labels = models.CharField(max_length=255, null=True, blank=True)
    artist_comments = models.IntegerField(null=True, blank=True)
    artist_favorites = models.IntegerField(null=True, blank=True)
    artist_date_created = models.CharField(max_length=255, null=True, blank=True)
    artist_flattr_name = models.CharField(max_length=255, null=True, blank=True)
    artist_paypal_name = models.CharField(max_length=255, null=True, blank=True)
    artist_latitude = models.FloatField(null=True, blank=True)
    artist_longitude = models.FloatField(null=True, blank=True)
    artist_image_file = models.CharField(max_length=255, null=True, blank=True)
    #artist_images = models.CharField(max_length=1000, null=True, blank=True)


    def __unicode__(self):
        return self.artist_name
 
class Albums(models.Model):
    album_id = models.IntegerField(null=True, blank=True)
    album_title = models.CharField(max_length=255, null=True, blank=True)
    album_handle = models.CharField(max_length=255, null=True, blank=True)
    album_url = models.URLField(max_length=255, null=True, blank=True)
    album_type = models.CharField(max_length=255, null=True, blank=True)
    artist = models.ForeignKey('main.Artists', null=True, blank=True)
    #artist_url = models.URLField(max_length=255, null=True, blank=True)
    album_producer = models.CharField(max_length=255, null=True, blank=True)
    album_engineer = models.CharField(max_length=255, null=True, blank=True)
    album_information = models.TextField(null=True, blank=True)
    album_date_released = models.CharField(max_length=255, null=True, blank=True)
    album_comments = models.IntegerField(null=True, blank=True)
    album_favorites = models.IntegerField(null=True, blank=True)
    album_tracks = models.IntegerField(null=True, blank=True)
    album_listens = models.IntegerField(null=True, blank=True)
    album_date_created = models.CharField(max_length=255, null=True, blank=True)
    album_image_file = models.CharField(max_length=255, null=True, blank=True)
    #album_images

    def __unicode__(self):
        return self.album_title

class Tracks(models.Model):
    track_id = models.CharField(max_length=255, null=True, blank=True)
    track_title = models.CharField(max_length=255, null=True, blank=True)
    track_url = models.TextField(null=True, blank=True)
    track_image_file = models.CharField(max_length=255, null=True, blank=True)
    artist = models.ForeignKey('main.Artists', null=True, blank=True)
    # artist_id = models.CharField(max_length=255, null=True, blank=True)
    # artist_name = models.CharField(max_length=255, null=True, blank=True)
    # artist_url = models.URLField(max_length=255, null=True, blank=True)
    # artist_website = models.URLField(max_length=255, null=True, blank=True)
    album = models.ForeignKey('main.Albums', null=True, blank=True)
    # album_id = models.IntegerField(null=True, blank=True)
    # album_title = models.CharField(max_length=255, null=True, blank=True)
    # album_url = models.URLField(max_length=255, null=True, blank=True)
    license_title = models.CharField(max_length=255, null=True, blank=True)
    license_url = models.URLField(max_length=255, null=True, blank=True)
    track_language_code = models.CharField(max_length=255, null=True, blank=True)
    track_duration = models.CharField(max_length=255, null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    track_disc_number = models.IntegerField(null=True, blank=True)
    track_explicit = models.CharField(max_length=255, null=True, blank=True)
    track_explicit_notes = models.CharField(max_length=255, null=True, blank=True)
    track_copyright_c = models.CharField(max_length=255, null=True, blank=True)
    track_copyright_p = models.CharField(max_length=255, null=True, blank=True)
    track_composer = models.CharField(max_length=255, null=True, blank=True)
    track_lyricist = models.CharField(max_length=255, null=True, blank=True)
    track_publisher = models.CharField(max_length=255, null=True, blank=True)
    track_instrumental = models.CharField(max_length=255, null=True, blank=True)
    track_information = models.TextField(null=True, blank=True)
    track_date_recorded = models.CharField(max_length=255, null=True, blank=True)
    track_comments = models.IntegerField(null=True, blank=True)
    track_favorites = models.IntegerField(null=True, blank=True)
    track_listens = models.IntegerField(null=True, blank=True)
    track_interest = models.IntegerField(null=True, blank=True)
    track_bit_rate = models.IntegerField(null=True, blank=True)
    track_date_created = models.CharField(max_length=255, null=True, blank=True)
    track_file = models.TextField(null=True, blank=True)
    license_image_file = models.CharField(max_length=255, null=True, blank=True)
    license_image_file_large = models.CharField(max_length=255, null=True, blank=True)
    license_parent_id = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.track_title


# class Artist(models.Model):

# class Albums(models.Model):

# class Tracks(models.Model): 