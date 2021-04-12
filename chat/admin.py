from django.contrib import admin
from chat.models import Chat, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Chat room admin"""
    list_display = ('creator', 'invited_user', 'date')

    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """Dialog for chat"""
    list_display = ('room', 'user', 'text', 'date')