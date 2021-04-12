from rest_framework import serializers

from chat.models import Room, Chat
from users.models import User


class UserChatSerializer(serializers.ModelSerializer):
    """Serializer for django model User"""

    class Meta:
        model = User
        fields = ('id', 'email')


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""
    user = UserChatSerializer()

    class Meta:
        model = Chat
        fields = ('id', 'user', 'text', 'date')
        read_only_fields = ('date',)


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for chat app models Room"""
    creator = UserChatSerializer()
    invited = UserChatSerializer(many=True)
    chat = ChatSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'creator', 'invited', 'date', 'chat',)
        read_only_fields = ('date',)


class ChatPostSerializers(serializers.ModelSerializer):
    """Serializer for chat messages"""
    room = RoomSerializer()
    user = UserChatSerializer()

    class Meta:
        model = Chat
        fields = ('room', 'text', 'user',)
