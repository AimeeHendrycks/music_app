#!/usr/bin/env python
import requests
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

import django
from django.conf import settings
from main.models import Albums, Artists

django.setup()

for art in Artists.objects.all():
    param_dict = {'api_key': settings.FMAKEY, 'limit':100, 'artist_id': art.artist_id}
    response = requests.get('https://freemusicarchive.org/api/get/albums.json', params=param_dict)
    try:
        response_dict = response.json()
        for data in response_dict['dataset']:
                if data.get('album_title') != None and str(unidecode(data.get('artist_name'))) == art.artist_name:
                    new_album, created = Albums.objects.get_or_create(album_title=str(unidecode(data.get('album_title'))))
                    new_album.album_id = data['album_id']
                    new_album.album_handle = str(data['album_handle'])
                    new_album.album_url = data['album_url']
                    new_album.album_type = str(data['album_type'])
                    if data.get('artist_name') != None:
                        try:
                            new_album.artist = Artists.objects.get(artist_name=str(unidecode(data.get('artist_name', ''))))
                        except Exception, e:
                            print 'No Such Artist!', e
                    else:
                        print "No ARTIST"
                    if data.get('album_producer') != None:
                        new_album.album_producer = str(unidecode(data.get('album_producer')))
                    else:
                        new_album.album_producer = ''
                    if data.get('album_engineer') != None:
                        new_album.album_engineer = str(unidecode(data.get('album_engineer', '')))
                    else:
                        new_album.album_engineer = ''
                    if data.get('album_information') != None:
                        new_album.album_information = str(unidecode(data.get('album_information', '')))
                    else:
                        new_album.album_information = ""
                    new_album.album_date_released = str(data['album_date_released'])
                    new_album.album_comments = data['album_comments']
                    new_album.album_favorites = data['album_favorites']
                    new_album.album_tracks = data['album_tracks']
                    new_album.album_listens = data['album_listens']
                    new_album.album_date_created = str(data['album_date_created'])
                    new_album.album_image_file = str(data['album_image_file'])

                    print data['album_title']
                    new_album.save()
    except Exception, e:
        print e