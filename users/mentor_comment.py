from django.db import models
from users.models import User


class MentorComment(models.Model):
    class Meta:
        verbose_name = 'Комментарий к ментору'
        verbose_name_plural = 'Комментарий к ментору'
        ordering = ['created']

    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.IntegerField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='mentor', null=True)
    users = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='commented_users', null=True, blank=True)

    def __str__(self):
        return f'{self.comment}'
