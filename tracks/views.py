from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request,'tracks/index.html',{'all_albums' : all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'tracks/detail.html', {'album' : album})

