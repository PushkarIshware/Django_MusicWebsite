from django.db import models


# Create your models here.

class Album(models.Model):
    # column names
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=400)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    # song is part of a album
    # so we create here primary and foreign key
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
