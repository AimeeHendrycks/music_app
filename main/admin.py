from django.contrib import admin
from main.models import Genres, Albums, Artists, Tracks, CustomUser

# Register your models here.
class GenresAdmin(admin.ModelAdmin):
    search_fields = ['genre_title']

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('album_title', 'artist')
    search_fields = ['album_title']

class ArtistsAdmin(admin.ModelAdmin):
    search_fields = ['artist_title']

class TracksAdmin(admin.ModelAdmin):
    list_display = ('track_title', 'album', 'artist')
    search_fields = ['track_title']

admin.site.register(Genres, GenresAdmin)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Artists, ArtistsAdmin)
admin.site.register(Tracks, TracksAdmin)
admin.site.register(CustomUser)
#do not register CustomUserManager
