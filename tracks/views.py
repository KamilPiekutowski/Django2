from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    print("index page")
    all_albums = Album.objects.all()
    return render(request,'tracks/index.html',{'all_albums' : all_albums})

def detail(request, album_id):
    print("details page")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'tracks/detail.html', {'album' : album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    print("favorite selected")
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'tracks/detail.html', {
            'album' : album,
            'error_message' : "Not a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'tracks/detail.html', {'album' : album})
