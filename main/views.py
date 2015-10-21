from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from main.forms import ContactForm, UserSignUp, UserLogin

from django.core.mail import send_mail
from django.conf import settings
from main.models import Genres, Artists, Albums, Tracks
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def genres_list(request):
    context = {}
    genre = request.GET.get('genre_title', None)
    print genre
    if genre != None:
        genres = Genres.objects.filter(genre_title__icontains=genre)
    else:
        genres = Genres.objects.all()

    context['genres'] = genres
    
    redirect('/genres_list/')

    return render_to_response('genres_list.html', context, context_instance=RequestContext(request))
    


class GenreDetailView(DetailView):
    model=Genres
    slug_field = 'genre_handle'
    template_name = 'genres_detail.html'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list/'

class GenreEditView(UpdateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_edit.html'
    success_url = '/genres_list/'

class GenreDeleteView(DeleteView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_delete.html'
    success_url = '/genres_list/'

def artists_list(request):
    context = {}
    artist = request.GET.get('artist_name', None)
    print artist
    if artist != None:
        artists = Artists.objects.filter(artist_name__icontains=artist)
    else:
        artists = Artists.objects.all()

    context['artists'] = artists
    redirect('/artists_list/')

    return render_to_response('artists_list.html', context, context_instance=RequestContext(request))

class ArtistDetailView(DetailView):
    model=Artists
    slug_field = 'artist_handle'
    template_name = 'artists_detail.html'

class ArtistCreateView(CreateView):
    model = Artists
    fields = '__all__'
    template_name = 'artists_create.html'
    success_url = '/artists_list/'

class ArtistEditView(UpdateView):
    model = Artists
    fields = '__all__'
    template_name = 'artists_edit.html'
    success_url = '/artists_list/'

class ArtistDeleteView(DeleteView):
    model = Artists
    fields = '__all__'
    template_name = 'artists_delete.html'
    success_url = '/artists_list/'

def albums_list(request):
    context = {}
    album = request.GET.get('album_title', None)
    print album
    if album != None:
        albums = Albums.objects.filter(album_title__icontains=album)
    else:
        albums = Albums.objects.all()

    context['albums'] = albums
    context['artists'] = Artists.objects.all()
    redirect('/albums_list/')

    return render_to_response('albums_list.html', context, context_instance=RequestContext(request))

class AlbumDetailView(DetailView):
    model=Albums
    slug_field = 'album_handle'
    template_name = 'albums_detail.html'

class AlbumCreateView(CreateView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_create.html'
    success_url = '/albums_list/'

class AlbumEditView(UpdateView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_edit.html'
    success_url = '/albums_list/'

class AlbumDeleteView(DeleteView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_delete.html'
    success_url = '/albums_list/'

def tracks_list(request):
    context = {}
    track = request.GET.get('track_title', None)
    print track
    if track != None:
        tracks = Tracks.objects.filter(track_title__icontains=track)
    else:
        tracks = Tracks.objects.all()

    context['tracks'] = tracks
    context['artists'] = Artists.objects.all()
    context['albums'] = Albums.objects.all()
    redirect('/tracks_list/')

    return render_to_response('tracks_list.html', context, context_instance=RequestContext(request))

class TrackDetailView(DetailView):
    model=Tracks
    template_name = 'tracks_detail.html'

class TrackCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_create.html'
    success_url = '/tracks_list/'

class TrackEditView(UpdateView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_edit.html'
    success_url = '/tracks_list/'

class TrackDeleteView(DeleteView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_delete.html'
    success_url = '/tracks_list/'

def base(request):
    context = {}
    context['albums'] = Albums.objects.all()
    context['genres'] = Genres.objects.all()
    context['artists'] = Artists.objects.all()
    context['tracks'] = Tracks.objects.all()
    return render_to_response('base.html', context, context_instance=RequestContext(request))

def home(request):
    context = {}
    context['albums'] = Albums.objects.all()
    context['genres'] = Genres.objects.all()
    context['artists'] = Artists.objects.all()
    context['tracks'] = Tracks.objects.all()
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def contact(request):
    context = {}
    if request.method =='POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('MUSICAPP MESSAGE FROM %s' % name, 
                message, email,
                [settings.EMAIL_HOST_USER], 
                fail_silently=False)
            context['message'] = "email sent"
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form
    return render_to_response('contact.html', context, context_instance=RequestContext(request))

def signup(request):

    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            print form.cleaned_data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                new_user = User.objects.create_user(username, email, password)
                context['valid'] = "Thank You For Signing Up!"
                new_user.save()
                auth_user = authenticate(username=username, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/home/')

            except Exception, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    elif request.method == 'GET':
        print 'GET'
        context['valid'] = "Please Sign Up!"

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_view(request):
    context = {}
    form = UserLogin()
    context['form'] = form

    if request.method == 'POST':
        print 'POST'
        context['form'] = UserLogin(request.POST)
        username = request.POST.get('username', None)
        print username
        password = request.POST.get('password', None)
        print password

        if username is not None and password is not None:
            print 'if worked'
            auth_user = authenticate(username=username, password=password)
            print 'auth worked'
            context['auth_user'] = auth_user
            if auth_user is not None and auth_user.is_active:
                print 'second if worked'
                login(request, auth_user)
                print 'login worked'
                context['outcome'] = "Login Successful"
                return HttpResponseRedirect('/home/')
            else:
                context['outcome'] = "Invalid User"
        else:
            context['outcome'] = "Please enter a User Name and/or Password"
    else:
        print 'GET'

    return render_to_response('login.html', context, context_instance=RequestContext(request))

def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/login/')

