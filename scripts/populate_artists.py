#!/usr/bin/env python
import requests
import sys
import os
from unidecode import unidecode
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

from main.models import Artists

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=60BLHNQCAOUFPIBZ&limit=8000')
try:
    response_dict = response.json()


    for data in response_dict['dataset']:
        if data.get('artist_name') != None:
            new_artist, created = Artists.objects.get_or_create(artist_name=str(unidecode(data.get('artist_name'))))

        new_artist.artist_handle = data['artist_handle']
        new_artist.artist_id = data['artist_id']
        new_artist.artist_url = data['artist_url']
        if data.get('artist_bio') != None:
            new_artist.artist_bio = str(unidecode(data.get('artist_bio')))
        else:
            new_artist.artist_bio = ''
        if data.get('artist_members'):
            new_artist.artist_members = str(unidecode(data.get('artist_members')))
        else:
            new_artist.artist_members = ''
        if data.get('artist_website') != None:
            new_artist.artist_website = str(unidecode(data.get('artist_website')))
        else:
            new_artist.artist_website = ''
        new_artist.artist_wikipedia_page = data['artist_wikipedia_page']
        if data.get('artist_donation_url', '') != None:
            new_artist.artist_donation_url = str(unidecode(data.get('artist_donation_url', '')))
        else:
            new_artist.artist_donation_url = ''
        if data.get('artist_contact','') != None:
            new_artist.artist_contact = str(unidecode(data.get('artist_contact', '')))
        else:
            new_artist.artist_contact = ''
        if data.get('artist_location') != None:
            new_artist.artist_location = str(unidecode(data.get('artist_location')))
        else:
            new_artist.artist_location = ''
        new_artist.artist_active_year_begin = data['artist_active_year_begin']
        new_artist.artist_active_year_end = data['artist_active_year_end']
        if data.get('artist_related_projects') != None:
            new_artist.artist_related_projects = str(unidecode(data.get('artist_related_projects')))
        else:
            new_artist.artist_related_projects = ''
        if data.get('artist_associated_labels') != None:
            new_artist.artist_associated_labels = str(unidecode(data.get('artist_associated_labels')))
        new_artist.artist_comments = data['artist_comments']
        new_artist.artist_favorites = data['artist_favorites']
        new_artist.artist_date_created = data['artist_date_created']
        new_artist.artist_flattr_name = data['artist_flattr_name']
        new_artist.artist_paypal_name = data['artist_paypal_name']
        new_artist.artist_latitude = data['artist_latitude']
        new_artist.artist_longitude = data['artist_longitude']
        new_artist.artist_image_file = data['artist_image_file']
        #new_artist.artist_images = data['artist_images']


        print data['artist_name']
        new_artist.save()
except Exception, e:
    print e