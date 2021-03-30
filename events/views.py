from rest_framework import generics, mixins

from events.models import Event, Comment
from events.serializers import EventSerializer, CommentSerializer, EventDetailSerializer


class EventAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'


class CommentsView(generics.ListCreateAPIView):
    """
    Bla bla
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'
