from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView, FormMixin
from main.forms import ContactForm, UserSignUp, UserLogin
from main.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
from main.models import Genres, Artists, Albums, Tracks
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from main.models import Artists
from main.serializers import ArtistSerializer, GenreSerializer, AlbumSerializer, TrackSerializer
from rest_framework import generics

# Create your views here.

class ArtistList(generics.ListCreateAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer


class TrackList(generics.ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer



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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                new_user = CustomUser.objects.create_user(email, password)
                                
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_view(request):
    context = {}
    form = UserLogin()
    context['form'] = form

    if request.method == 'POST':
        form = UserLogin(request.POST)
        context['form'] = form
        print "validating"
        if form.is_valid():
            print "am i valid?"

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth_user = authenticate(email=email, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Invalid User"
        else:
            context['valid'] = "Please enter an Email and Password"
    else:
        print 'GET'

    return render_to_response('login.html', context, context_instance=RequestContext(request))

def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/login/')

class GenreListView(ListView):
    template_name = 'genres_list.html'
    paginate_by =20
    def get_queryset(self):
        if 'search' in self.request.GET:
            object_list = Genres.objects.filter(genre_title__icontains=self.request.GET['search'])
        else:
            object_list = Genres.objects.all()
        print object_list
        return object_list


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


class ArtistListView(ListView):
    template_name = 'artists_list.html'
    paginate_by =20
    def get_queryset(self):
        if 'search' in self.request.GET:
            object_list = Artists.objects.filter(artist_name__icontains=self.request.GET['search'])
        else:
            object_list = Artists.objects.all()
        print object_list
        return object_list

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


class AlbumListView(ListView):
    template_name = 'albums_list.html'
    paginate_by =20
    def get_queryset(self):
        if 'search' in self.request.GET:
            object_list = Albums.objects.filter(album_title__icontains=self.request.GET['search'])
        else:
            object_list = Albums.objects.all()
        print object_list
        return object_list

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

class TrackListView(ListView):
    template_name = 'tracks_list.html'
    paginate_by =20
    def get_queryset(self):
        if 'search' in self.request.GET:
            object_list = Tracks.objects.filter(track_title__icontains=self.request.GET['search'])
        else:
            object_list = Tracks.objects.all()
        print object_list
        return object_list

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

#tracks
def json_response(request):
    search_string = request.GET.get('search', '')
    objects = Tracks.objects.filter(track_title__icontains=search_string) 
    object_list = []
    for obj in objects:
        object_list.append({'track_title':obj.track_title, 'track_image_file': obj.track_image_file})

    return JsonResponse(object_list, safe=False)

def ajax_search(request):
    context = {}

    return render_to_response('ajax_template.html', context, context_instance=RequestContext(request))



#{'track_image_file': obj.track_image_file, 'artist': obj.artist.artist_name, 'album':obj.album.album_title}