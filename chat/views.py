from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, mixins
from django.contrib.auth.models import User
from chat.models import Chat, Room
from chat.serializers import ChatSerializer, ChatPostSerializers, \
    RoomSerializer, UserChatSerializer


class Rooms(APIView):
    """Chat rooms APIView with get and post methods"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(
            Q(creator=request.user) |
            Q(invited=request.user))
        serializers = RoomSerializer(rooms,
                                     many=True)
        return Response({'data': serializers.data})

    def post(self, request):
        Room.objects.create(creator=request.user)
        return Response(status=201)

class Dialog(APIView):
    """Dialog for chat and messages using get and post methods"""
    permission_classes = [permissions.IsAuthenticated, ]
    permissions_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        room = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(room, status=201)
        else:
            return Response(status=400)


class AddUserRoom(APIView):
    """Add users to the chat rooms"""

    def get(self, request):
        users = User.objects.all()
        serializers = UserChatSerializer(users,
                                     many=True)
        return Response(serializers.data)

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)
