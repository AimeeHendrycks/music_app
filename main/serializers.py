from rest_framework import serializers
from main.models import Artists, Genres, Albums, Tracks


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ('artist_id', 'artist_handle', 'artist_name', 'artist_url', 'artist_bio', 'artist_image_file', 'artist_website', 'artist_members', 'artist_wikipedia_page', 'artist_donation_url', 'artist_contact', 'artist_location', 'artist_active_year_begin', 'artist_active_year_end', 'artist_related_projects', 'artist_associated_labels', 'artist_comments', 'artist_favorites', 'artist_date_created', 'artist_flattr_name', 'artist_paypal_name', 'artist_latitude', 'artist_longitude', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('genre_title', 'genre_id', 'genre_parent_id', 'genre_handle')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ('album_id', 'album_title', 'album_tracks', 'album_handle', 'album_url', 'artist', 'album_producer', 'album_engineer', 'album_information', 'album_date_released', 'album_comments', 'album_favorites', 'album_tracks', 'album_listens', 'album_date_created', 'album_image_file')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = ('track_id', 'track_title', 'track_url', 'track_image_file', 'artist', 'album', 'license_title', 'license_url', 'track_language_code', 'track_duration', 'track_number', 'track_disc_number', 'track_explicit', 'track_explicit_notes', 'track_copyright_c', 'track_copyright_p', 'track_composer', 'track_lyricist', 'track_publisher', 'track_instrumental', 'track_information', 'track_date_recorded', 'track_comments', 'track_favorites', 'track_listens', 'track_interest', 'track_bit_rate', 'track_date_created', 'track_file', 'license_image_file', 'license_image_file_large', 'license_parent_id')