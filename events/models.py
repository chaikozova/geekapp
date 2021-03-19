from django.db import models


class Event(models.Model):
    class Meta:
        verbose_name = 'Меропрятие'
        verbose_name_plural = 'Меропрятия'
    image = models.ImageField(upload_to='media', max_length=240, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    date_of_event = models.DateTimeField()
    location = models.CharField(max_length=255)
    ratting = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)


class Comment(models.Model):
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)
    rate = models.IntegerField()
    events = models.ForeignKey(Event,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='comments')