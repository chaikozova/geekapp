from django.db import models

from users.models import User


class Event(models.Model):
    class Meta:
        verbose_name = 'Меропрятие'
        verbose_name_plural = 'Меропрятия'
    image = models.ImageField(upload_to='media', max_length=240, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_event = models.DateTimeField()
    location = models.CharField(max_length=255)
    ratting = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментария'
        ordering = ['created']
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    rate = models.IntegerField(null=True, blank=True)
    events = models.ForeignKey(Event, on_delete=models.SET_NULL,
                               null=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
