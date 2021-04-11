from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Room, Chat
from chat.serializers import RoomSerializer, ChatSerializer, ChatPostSerializers, UserChatSerializer
from users.models import User


class RoomsView(APIView):
    """Chat rooms APIView with get and post methods"""
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) |
                                    Q(invited=request.user))
        serializers = RoomSerializer(rooms, many=True)
        return Response(data=serializers.data)

    def post(self, request):
        room = Room.objects.create(creator=request.user)
        room.save()
        return Response(data=self.RoomSerializer(room).data,
                        status=status.HTTP_201_CREATED)


class RoomDetailView(APIView):
    allowed_methods = ['get', 'delete']
    serializer_class = RoomSerializer

    def get(self, request, id):
        room = Room.objects.get(id=id)
        return Response(data=self.serializer_class(room, many=False).data)

    def delete(self, request, id):
        room = Room.objects.get(id=id)
        room.delete()
        room = Room.objects.all()
        return Response(data=self.serializer_class(room, many=True).data)


class ChatsView(APIView):
    allowed_methods = ['get', 'post']
    serializer_class = ChatSerializer

    def post(self, request, id):
        room = Room.objects.get(id=id)
        #message = request.data.get('text')
        chat = Chat.objects.create_or_update(user=request.user,
                                             room=room)
        chat.save()
        return Response(data=self.serializer_class(chat).data,
                        status=status.HTTP_201_CREATED)

    def get(self, request, id):
        room = Room.objects.get(id=id)
        chat = Chat.objects.filter(room=room)
        return Response(data=self.serializer_class(chat,
                                                   many=True).data)


class ChatDetailView(APIView):
    allowed_methods = ['get', 'put', 'delete']
    serializer_class = ChatSerializer

    # def put(self, request, pk, id):
    #     room = Room.objects.get(pk=pk)
    #     chat = Chat.objects.get(room=room, id=id)
    #     message = request.data.get('text')
    #     chat = Chat.objects.update(id=id,
    #                                user=request.user,
    #                                room=room,
    #                                text=message)
    #     chat.save()
    #     return Response(data=self.serializer_class(chat).data,
    #                     status=status.HTTP_201_CREATED)

    def get(self, request, pk, id):
        room = Room.objects.get(pk=pk)
        try:
            chat = Chat.objects.get(id=id, room=room)
        except Chat.DoesNotExist:
            return Response({'message': 'chat does not exist'})

        return Response(data=self.serializer_class(chat,
                                                   many=False).data)

    def delete(self, request, pk, id):
        room = Room.objects.get(pk=pk)
        try:
            chat = Chat.objects.get(id=id, room=room)
        except Chat.DoesNotExist:
            return Response({'message': 'chat does not exist'})
        chat.delete()
        chat = Chat.objects.all()
        return Response(data=self.serializer_class(chat,
                                                   many=True).data)


class DialogView(APIView):
    """Dialog for chat and messages using get and post methods"""

    # permission_classes = [permissions.IsAuthenticated, ]
    # permissions_classes = [permissions.AllowAny, ]
    allowed_methods = ['get', 'post']

    def get(self, request, pk, id):
        room = Room.objects.get(pk=pk)
        chat = Chat.objects.filter(room=room, id=id)
        serializer = ChatSerializer(chat, many=True)
        return Response(data=serializer.data)

    def post(self, request, pk, id):
        room = Room.objects.get(pk=pk)
        dialog = ChatPostSerializers(room=room,
                                     data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(data=dialog.data, status=201)
        else:
            return Response(status=400)


class AddUserRoom(APIView):
    """Add users to the chat rooms"""

    def get(self, request):
        room = request.data.get('room')
        room = Room.objects.get(id=room)
        serializers = RoomSerializer(room)
        return Response(serializers.data)

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        room = Room.objects.get(id=room)
        room.invited.add(user)
        room.save()
        return Response(data=RoomSerializer(room).data, status=201)

