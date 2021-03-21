from rest_framework import generics, mixins

from events.models import Event, Comment
from events.serializers import EventSerializer, CommentSerializer, EventDetailSerializer


class EventAPIView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'


class CommentView(generics.ListCreateAPIView):
    """
    Bla bla
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
