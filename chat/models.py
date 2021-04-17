from django.db import models

from users.models import User


class Room(models.Model):
    """Model of chat room"""
    name = models.TextField(verbose_name='Наименование чата', null=True, blank=True)
    creator = models.ForeignKey(User, verbose_name='Creator', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Invited', related_name='invited_user')
    date = models.DateField('Date of creation', auto_now_add=True)

    class Meta:
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'


class Chat(models.Model):
    """Chat model"""
    room = models.ForeignKey(Room, verbose_name='Chat Room', on_delete=models.CASCADE, related_name='chat_room')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField('Date of sent message', auto_now_add=True)

    class Meta:
        verbose_name = 'Chat\'s message'
        verbose_name_plural = 'Chat\'s messages'