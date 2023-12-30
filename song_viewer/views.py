from django.shortcuts import render, get_object_or_404
from .models import Song
# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'song_viewer/home.html', {'songs':songs})

def detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song_lyrics = song.lyrics.split("\r\n")
    verse_length = (song_lyrics.index("V2") - song_lyrics.index("V1"))
    print(verse_length)
    return render(request, 'song_viewer/detail.html', {'song':song_lyrics,'verse_length':verse_length})