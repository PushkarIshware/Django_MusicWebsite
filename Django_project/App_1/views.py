
from django.shortcuts import render, get_object_or_404

from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    content = {"all_albums": all_albums, }
    return render(request, "App_1/index.html", content)

    # -----------------------------------------------------------------------------
    # HARDCODING (WE ARE NOT USING TEMPLATES...THATS WHY WE WRITE EVERYTHING HERE)
    # all_albums = Album.objects.all()
    # html = ""
    # for album in all_albums:
    #     url = '/App_1/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    # return HttpResponse(html)
    # ------------------------------------------------------------------------------


def detail(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'App_1/detail.html', {"album": album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'App_1/detail.html', {"album": album,
                                                     "error": "Select song atleast"})

    else:
        selected_song.favorite = True
        selected_song.save()
        return render(request, 'App_1/detail.html', {"album": album})



