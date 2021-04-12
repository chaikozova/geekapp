from django.db import models

from users.models import User


class Event(models.Model):
    class Meta:
        verbose_name = 'Меропрятие'
        verbose_name_plural = 'Меропрятия'

    image = models.ImageField(upload_to='media', max_length=240, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_event = models.DateField(null=True, blank=True)
    time_of_event = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255)
    dop_location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)

    @property
    def rating_average(self):
        rating = self.comments.aggregate(models.Avg('rate')).get('rate__avg')
        try:
            rating = float("{:.1f}".format(rating))
        except TypeError:
            rating = 0.0
        return rating

    @property
    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментария'
        ordering = ['created']

    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.IntegerField(null=True, blank=True)
    events = models.ForeignKey(Event, on_delete=models.SET_NULL,
                               null=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return f'{self.events.title} - {self.comment}'
