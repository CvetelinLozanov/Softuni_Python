from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
    )

    image_url = models.URLField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(
        max_length=50
    )

    music_file_data = models.FileField()

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        related_name='songs'
    )

    def __str__(self):
        return self.song_name