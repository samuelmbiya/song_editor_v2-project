from django.shortcuts import render, get_object_or_404
from .models import Song
# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'song_viewer/home.html', {'songs':songs})

def detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'song_viewer/detail.html', {'song':song})