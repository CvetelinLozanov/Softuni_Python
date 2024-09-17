from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SongCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from .models import Album, Song


# Create your views here.
def index(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'common/index.html', context)


def create_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form
    }

    return render(request, 'albums/create-album.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        album.delete()
        return redirect('index')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'albums/delete-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, 'albums/album-details.html', context)


def create_song(request):

    if request.method == 'GET':
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form
    }

    return render(request, 'songs/create-song.html', context)


def play_song(request, pk):
    song = Song.objects.get(pk=pk)

    context = {
        'song': song,
    }

    return render(request, 'songs/music-player.html', context)


def serve_song(request, pk):
    song = Song.objects.get(pk=pk)

    if song:
        response = HttpResponse(song.music_file_data, content_type="audio/mpeg")
        response["Content-Disposition"] = f'inline; filename="{song.song_name}"'
        return response
    else:
        return HttpResponse('Song not found', status=404)
