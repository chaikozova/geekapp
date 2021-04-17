from rest_framework import serializers

from chat.models import Room, Chat
from courses.serializers import GroupNameSerializer
from users.models import User


class UserChatSerializer(serializers.ModelSerializer):
    """Serializer for django model User"""
    group_number = GroupNameSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'group_number')


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""
    user = UserChatSerializer()

    class Meta:
        model = Chat
        fields = ('id', 'user', 'text', 'date')
        read_only_fields = ('date',)


class RoomListSerializer(serializers.ModelSerializer):
    """
    Serializer for a list of Chats (Request)
    """
    creator = UserChatSerializer()

    class Meta:
        model = Room
        fields = ('id', 'name', 'creator', 'date')


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for chat app models Room"""
    creator = UserChatSerializer()
    invited = UserChatSerializer(many=True)
    chat = ChatSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'creator', 'invited', 'date', 'chat',)
        read_only_fields = ('date',)


class ChatPostSerializers(serializers.ModelSerializer):
    """Serializer for chat messages"""
    room = RoomSerializer()
    user = UserChatSerializer()

    class Meta:
        model = Chat
        fields = ('room', 'text', 'user',)
