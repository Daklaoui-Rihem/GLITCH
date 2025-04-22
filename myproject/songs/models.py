from django.db import models

# songs/models.py
from django.db import models

class Song(models.Model):
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip_hop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='other')
    cover = models.ImageField(upload_to='song_covers/', blank=True, null=True)
    audio_file = models.FileField(upload_to='song_files/')
    is_famous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
