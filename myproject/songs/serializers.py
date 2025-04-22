# songs/serializers.py
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'genre', 'cover', 'audio_file', 'is_famous', 'created_at']