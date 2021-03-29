from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Chat, Room

class UserChatSerializer(serializers.ModelSerializer):
    """Serializer for django model User"""
    class Meta:
        model = User
        fields = ('id', 'email')


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for chat app models Room"""
    creator = UserChatSerializer()
    invited = UserChatSerializer(many=True)

    class Meta:
        model = Room
        fields = ('id', 'creator', 'invited', 'date')


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""
    user = UserChatSerializer()
    room = RoomSerializer()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
    """Serializer for chat messages"""
    room = RoomSerializer()
    user = UserChatSerializer()



    class Meta:
        model = Chat
        fields = ('room', 'text')