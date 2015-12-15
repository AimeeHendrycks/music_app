"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.edit import CreateView
from main.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^artists/$', views.ArtistList.as_view()),
    url(r'^artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view()),
    url(r'^genres/$', views.GenreList.as_view()),
    url(r'^genres/(?P<pk>[0-9]+)/$', views.GenreDetail.as_view()),
    url(r'^albums/$', views.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^tracks/$', views.TrackList.as_view()),
    url(r'^tracks/(?P<pk>[0-9]+)/$', views.TrackDetail.as_view()),

    url(r'^json_response/$', views.json_response),
    url(r'^ajax_search/$', views.ajax_search),

    url(r'^genres_list/$', views.GenreListView.as_view()),
#   url(r'^genres_detail/(?P<pk>\d+)/$', views.GenreDetailView.as_view())
    url(r'^genres_detail/(?P<pk>\d+)/$', views.GenreDetailView.as_view()),
    url(r'^genres_create/$', views.GenreCreateView.as_view()),
    url(r'^genres_edit/(?P<pk>\d+)/$', views.GenreEditView.as_view()),
    url(r'^genres_delete/(?P<pk>\d+)/$', views.GenreDeleteView.as_view()),

    url(r'^artists_list/$', views.ArtistListView.as_view()),
    url(r'^artists_detail/(?P<pk>\d+)/$', views.ArtistDetailView.as_view()),
    url(r'^artists_create/$', views.ArtistCreateView.as_view()),
    url(r'^artists_edit/(?P<pk>\d+)/$', views.ArtistEditView.as_view()),  
    url(r'^artists_delete/(?P<pk>\d+)/$', views.ArtistDeleteView.as_view()),    

    url(r'^albums_list/$', views.AlbumListView.as_view()),
    url(r'^albums_detail/(?P<pk>\d+)/$', views.AlbumDetailView.as_view()),
    url(r'^albums_create/$', views.AlbumCreateView.as_view()),
    url(r'^albums_edit/(?P<pk>\d+)/$', views.AlbumEditView.as_view()),
    url(r'^albums_delete/(?P<pk>\d+)/$', views.AlbumDeleteView.as_view()),

    url(r'^tracks_list/$', views.TrackListView.as_view()),
    url(r'^tracks_detail/(?P<pk>\d+)/$', views.TrackDetailView.as_view()),
    url(r'^tracks_create/$', views.TrackCreateView.as_view()),
    url(r'^tracks_edit/(?P<pk>\d+)/$', views.TrackEditView.as_view()),
    url(r'^tracks_delete/(?P<pk>\d+)/$', views.TrackDeleteView.as_view()),

    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/$', views.login_view),
    url(r'^contact/$', views.contact),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^signup/$', views.signup),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # url(r'^login/$',auth_views.login, {'template_name': 'login.html'}),
    # url(r'^logout/$','django.contrib.auth.views.logout'),

    url(r'^register/$', CreateView.as_view(template_name='register.html',
                                            form_class=CustomUserCreationForm,
                                            success_url='/')),

]


urlpatterns = format_suffix_patterns(urlpatterns)