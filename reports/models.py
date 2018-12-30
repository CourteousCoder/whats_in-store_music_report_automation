from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True)


class Song(models.Model):
    artists = models.ManyToManyField(Artist)
    title = models.CharField(max_length=255)
    mri_media_id = models.CharField(max_length=32)


class Store(models.Model):
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=127)
    mri_player_id = models.IntegerField()


class Spin(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    store = models.ManyToManyField(Store)
    date_played = models.DateField()
    spin_count = models.IntegerField()
