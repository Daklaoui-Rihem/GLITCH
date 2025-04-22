# songs/views.py
from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned songs by filtering against
        query parameters in the URL
        """
        queryset = Song.objects.all()
        
        # Filter by genre
        genre = self.request.query_params.get('genre', None)
        if genre:
            queryset = queryset.filter(genre=genre)
            
        # Filter by famous status
        is_famous = self.request.query_params.get('is_famous', None)
        if is_famous is not None:
            is_famous_bool = is_famous.lower() in ['true', '1', 'yes']
            queryset = queryset.filter(is_famous=is_famous_bool)
            
        # Filter by artist
        artist = self.request.query_params.get('artist', None)
        if artist:
            queryset = queryset.filter(artist__icontains=artist)
            
        return queryset