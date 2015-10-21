#!/usr/bin/env python
import requests
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

import django
from django.conf import settings
from main.models import Tracks, Artists, Albums

for alb in Albums.objects.all():
    param_dict = {'api_key': settings.FMAKEY, 'limit':100, 'album_id': alb.album_id}
    response = requests.get('https://freemusicarchive.org/api/get/tracks.json', params=param_dict)
    try:
        response_dict = response.json()


        for data in response_dict['dataset']:
            
                if data.get('track_title', '') != None and data.get('album_title', '') != None and str(unidecode(data.get('album_title', ''))) == alb.album_title:
                    new_track, created = Tracks.objects.get_or_create(track_title=str(unidecode(data.get('track_title', ''))))
                    
                    new_track.artist = alb.artist
                    new_track.album = alb
                    new_track.track_id = data['track_id']
                    new_track.track_url = data['track_url']
                    new_track.track_image_file = data['track_image_file'] 
                    new_track.license_title = data['license_title']
                    new_track.license_url = data['license_url']
                    new_track.track_language_code = data['track_language_code']
                    new_track.track_duration = data['track_duration']
                    new_track.track_number = data['track_number']
                    new_track.track_disc_number = data['track_disc_number']
                    new_track.track_explicit = data['track_explicit']
                    new_track.track_explicit_notes = data['track_explicit_notes']
                    new_track.track_copyright_c = data['track_copyright_c']
                    new_track.track_copyright_p = data['track_copyright_p']
                    if data.get('track_composer')!= None:
                        new_track.track_composer = str(unidecode(data.get('track_composer')))
                    else:
                        new_track.track_composer = ''
                    new_track.track_lyricist = data['track_lyricist']
                    new_track.track_publisher = data['track_publisher']
                    new_track.track_instrumental = data['track_instrumental']
                    if data.get('track_information') != None:
                        new_track.track_information = str(unidecode(data.get('track_information')))
                    else:
                        new_track.track_information = ''
                    new_track.track_date_recorded = data['track_date_recorded']
                    new_track.track_comments = data['track_comments']
                    new_track.track_favorites = data['track_favorites']
                    new_track.track_listens = data['track_listens']
                    new_track.track_interest = data['track_interest']
                    new_track.track_bit_rate = data['track_bit_rate']
                    new_track.track_date_created = data['track_date_created']
                    new_track.track_file = data['track_file']           
                    new_track.license_image_file = data['license_image_file']
                    new_track.license_image_file_large = data['license_image_file_large']
                    new_track.license_parent_id = data['license_parent_id']
                    
                    print data['track_title']
                    new_track.save()
                else:
                    pass
    except Exception, e:
        print e